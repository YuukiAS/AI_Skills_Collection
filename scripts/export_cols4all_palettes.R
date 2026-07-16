#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

get_arg <- function(flag, default = NULL) {
  idx <- match(flag, args)
  if (is.na(idx) || idx == length(args)) {
    return(default)
  }
  args[[idx + 1]]
}

out_path <- get_arg("--out", "palette/external/cols4all-palettes.json")
repo_commit <- get_arg("--repo-commit", NA_character_)
source_repo <- get_arg("--source-repo", "https://github.com/cols4all/cols4all-R")
access_date <- get_arg("--access-date", format(Sys.Date(), "%Y-%m-%d"))

temp_lib <- Sys.getenv("AI_SKILLS_R_LIB", unset = "")
if (nzchar(temp_lib)) {
  .libPaths(c(temp_lib, .libPaths()))
}

suppressPackageStartupMessages(library(cols4all))

json_escape <- function(x) {
  x <- ifelse(is.na(x), "", as.character(x))
  x <- gsub("\\\\", "\\\\\\\\", x)
  x <- gsub("\"", "\\\\\"", x)
  x <- gsub("\r", "\\r", x)
  x <- gsub("\n", "\\n", x)
  x <- gsub("\t", "\\t", x)
  paste0("\"", x, "\"")
}

json_scalar <- function(x) {
  if (length(x) == 0 || is.null(x) || is.na(x)) {
    return("null")
  }
  if (is.logical(x)) {
    return(ifelse(x, "true", "false"))
  }
  if (is.numeric(x)) {
    if (!is.finite(x)) return("null")
    return(as.character(x))
  }
  json_escape(x)
}

json_array <- function(x) {
  if (length(x) == 0 || is.null(x)) {
    return("[]")
  }
  paste0("[", paste(vapply(as.character(x), json_escape, character(1)), collapse = ","), "]")
}

json_object <- function(named_values) {
  parts <- vapply(names(named_values), function(name) {
    paste0(json_escape(name), ":", named_values[[name]])
  }, character(1))
  paste0("{", paste(parts, collapse = ","), "}")
}

normalise_colors <- function(colors) {
  if (is.null(colors)) return(character(0))
  if (is.matrix(colors) || is.data.frame(colors)) {
    colors <- as.vector(as.matrix(colors))
  }
  colors <- unique(as.character(colors))
  colors[grepl("^#[0-9A-Fa-f]{6}$", colors)]
}

pick_n <- function(info) {
  n <- suppressWarnings(as.numeric(info$ndef))
  if (!is.finite(n) || is.na(n) || n < 1) {
    n <- suppressWarnings(as.numeric(info$nmax))
  }
  if (!is.finite(n) || is.na(n) || n < 1) {
    n <- switch(info$type, cat = 8, seq = 9, div = 11, cyc = 12, 9)
  }
  n <- min(max(as.integer(round(n)), 1), 16)
  n
}

score_row <- function(name, n) {
  row <- tryCatch(c4a_scores(name, n = n, no.match = "error", verbose = FALSE), error = function(e) NULL)
  if (is.null(row) || nrow(row) < 1) return(list())
  row <- row[1, , drop = FALSE]
  fields <- c(
    "cbfriendly", "fairness", "min_dist", "CRmin", "CRwt", "CRbk",
    "Blues", "Hspread", "fair", "contrastWT", "contrastBK", "equiluminance"
  )
  result <- list()
  for (field in fields) {
    if (field %in% names(row)) {
      value <- row[[field]][1]
      if (is.logical(value)) {
        result[[field]] <- ifelse(value, "true", "false")
      } else if (is.numeric(value)) {
        result[[field]] <- ifelse(is.finite(value), as.character(round(value, 4)), "null")
      } else {
        result[[field]] <- json_escape(as.character(value))
      }
    }
  }
  result
}

series_table <- c4a_series()
series_objects <- apply(series_table, 1, function(row) {
  json_object(list(series = json_escape(row[["series"]]), description = json_escape(row[["description"]])))
})

type_table <- c4a_types()
type_objects <- apply(type_table, 1, function(row) {
  json_object(list(type = json_escape(row[["type"]]), description = json_escape(row[["description"]])))
})

palettes <- c4a_palettes(type = "all", full.names = TRUE)
palette_objects <- character(0)
failures <- character(0)

for (palette_name in palettes) {
  info <- tryCatch(c4a_info(palette_name, no.match = "error", verbose = FALSE), error = function(e) e)
  if (inherits(info, "error")) {
    failures <- c(failures, paste0(palette_name, ": ", conditionMessage(info)))
    next
  }

  n <- pick_n(info)
  colors <- tryCatch(normalise_colors(c4a(palette_name, n)), error = function(e) character(0))
  if (!length(colors)) {
    failures <- c(failures, paste0(palette_name, ": no exportable hex colors"))
    next
  }

  score <- score_row(palette_name, n)
  score_json <- if (length(score)) json_object(score) else "{}"

  palette_objects <- c(palette_objects, json_object(list(
    id = json_escape(paste0("cols4all.", palette_name)),
    source_id = json_escape(palette_name),
    name = json_escape(info$name),
    series = json_escape(info$series),
    type = json_escape(info$type),
    n = json_scalar(n),
    nmin = json_scalar(suppressWarnings(as.numeric(info$nmin))),
    nmax = json_scalar(suppressWarnings(as.numeric(info$nmax))),
    colors = json_array(colors),
    na_color = json_scalar(info$na),
    license = json_escape("GPL-3"),
    provenance_status = json_escape("copied_from_cols4all_runtime_export"),
    scores = score_json,
    citation = json_scalar(info$cit),
    bibtex = json_scalar(info$bib)
  )))
}

doc <- json_object(list(
  library_id = json_escape("cols4all-palettes"),
  generated_on = json_escape(format(Sys.time(), "%Y-%m-%dT%H:%M:%S%z")),
  package = json_escape("cols4all"),
  package_version = json_escape(as.character(packageVersion("cols4all"))),
  source_repo = json_escape(source_repo),
  source_commit = json_scalar(repo_commit),
  access_date = json_escape(access_date),
  license = json_escape("GPL-3"),
  usage_note = json_escape("Palette color values were exported from the GPL-3 cols4all R package. Keep license/provenance visible when redistributing plugin payloads."),
  series = paste0("[", paste(series_objects, collapse = ","), "]"),
  types = paste0("[", paste(type_objects, collapse = ","), "]"),
  palettes = paste0("[", paste(palette_objects, collapse = ","), "]"),
  failures = json_array(failures)
))

dir.create(dirname(out_path), recursive = TRUE, showWarnings = FALSE)
writeLines(doc, out_path, useBytes = TRUE)
cat("wrote", out_path, "with", length(palette_objects), "palettes and", length(failures), "failures\n")
