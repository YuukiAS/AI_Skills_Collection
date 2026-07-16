#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

get_arg <- function(flag, default = NULL) {
  idx <- match(flag, args)
  if (is.na(idx) || idx == length(args)) {
    return(default)
  }
  args[[idx + 1]]
}

input_path <- get_arg("--input", "palette/scientific-figure-palettes.json")
out_path <- get_arg("--out", "palette/cols4all-evaluation.json")
access_date <- get_arg("--access-date", format(Sys.Date(), "%Y-%m-%d"))

temp_lib <- Sys.getenv("AI_SKILLS_R_LIB", unset = "")
if (nzchar(temp_lib)) {
  .libPaths(c(temp_lib, .libPaths()))
}

suppressPackageStartupMessages(library(cols4all))

text <- paste(readLines(input_path, warn = FALSE, encoding = "UTF-8"), collapse = "\n")

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
  if (length(x) == 0 || is.null(x) || is.na(x)) return("null")
  if (is.logical(x)) return(ifelse(x, "true", "false"))
  if (is.numeric(x)) {
    if (!is.finite(x)) return("null")
    return(as.character(round(x, 4)))
  }
  json_escape(x)
}

json_array <- function(x) {
  if (length(x) == 0 || is.null(x)) return("[]")
  paste0("[", paste(vapply(as.character(x), json_escape, character(1)), collapse = ","), "]")
}

json_object <- function(named_values) {
  parts <- vapply(names(named_values), function(name) {
    paste0(json_escape(name), ":", named_values[[name]])
  }, character(1))
  paste0("{", paste(parts, collapse = ","), "}")
}

extract_palette_blocks <- function(raw_text) {
  starts <- gregexpr("\\{\\s*\"id\"\\s*:", raw_text, perl = TRUE)[[1]]
  if (starts[1] == -1) return(character(0))
  blocks <- character(0)
  for (start in starts) {
    depth <- 0
    in_string <- FALSE
    escaped <- FALSE
    chars <- strsplit(substr(raw_text, start, nchar(raw_text)), "", fixed = TRUE)[[1]]
    for (i in seq_along(chars)) {
      ch <- chars[[i]]
      if (in_string) {
        if (escaped) {
          escaped <- FALSE
        } else if (ch == "\\") {
          escaped <- TRUE
        } else if (ch == "\"") {
          in_string <- FALSE
        }
      } else {
        if (ch == "\"") {
          in_string <- TRUE
        } else if (ch == "{") {
          depth <- depth + 1
        } else if (ch == "}") {
          depth <- depth - 1
          if (depth == 0) {
            blocks <- c(blocks, substr(raw_text, start, start + i - 1))
            break
          }
        }
      }
    }
  }
  blocks
}

extract_string <- function(block, key) {
  pattern <- paste0("\"", key, "\"\\s*:\\s*\"((?:[^\"\\\\]|\\\\.)*)\"")
  m <- regexec(pattern, block, perl = TRUE)
  hit <- regmatches(block, m)[[1]]
  if (length(hit) < 2) return(NA_character_)
  gsub("\\\\\"", "\"", hit[[2]])
}

extract_colors <- function(block) {
  m <- regmatches(block, gregexpr("\"#[0-9A-Fa-f]{6}\"", block, perl = TRUE))[[1]]
  if (!length(m) || m[1] == -1) return(character(0))
  unique(gsub("\"", "", m))
}

score_palette <- function(id, colors, type) {
  types <- switch(type, categorical = "cat", sequential = "seq", diverging = "div", cyclic = "cyc", "cat")
  palette_list <- list(colors)
  names(palette_list) <- id
  data <- c4a_data(
    palette_list,
    types = types,
    series = "ai_skills",
    nmin = length(colors),
    nmax = length(colors),
    ndef = length(colors),
    format.palette.name = FALSE,
    remove.blacks = FALSE,
    remove.whites = FALSE,
    remove.names = TRUE
  )
  c4a_load(data, overwrite = TRUE)
  fullname <- paste0("ai_skills.", id)
  row <- tryCatch(c4a_scores(fullname, n = length(colors), no.match = "error", verbose = FALSE), error = function(e) NULL)
  if (is.null(row) || nrow(row) < 1) {
    return(json_object(list(id = json_escape(id), error = json_escape("cols4all scoring failed"))))
  }
  row <- row[1, , drop = FALSE]
  fields <- c(
    "cbfriendly", "fairness", "min_dist", "CRmin", "CRwt", "CRbk",
    "Blues", "Hspread", "fair", "contrastWT", "contrastBK", "equiluminance"
  )
  score_parts <- list()
  for (field in fields) {
    if (field %in% names(row)) {
      score_parts[[field]] <- json_scalar(row[[field]][1])
    }
  }
  json_object(list(
    id = json_escape(id),
    type = json_escape(type),
    n = json_scalar(length(colors)),
    colors = json_array(colors),
    scores = json_object(score_parts)
  ))
}

blocks <- extract_palette_blocks(text)
objects <- character(0)
for (block in blocks) {
  id <- extract_string(block, "id")
  type <- extract_string(block, "type")
  colors <- extract_colors(block)
  if (is.na(id) || !length(colors)) next
  objects <- c(objects, tryCatch(score_palette(id, colors, type), error = function(e) {
    json_object(list(id = json_escape(id), error = json_escape(conditionMessage(e))))
  }))
}

doc <- json_object(list(
  library_id = json_escape("cols4all-evaluation"),
  generated_on = json_escape(format(Sys.time(), "%Y-%m-%dT%H:%M:%S%z")),
  input = json_escape(input_path),
  package = json_escape("cols4all"),
  package_version = json_escape(as.character(packageVersion("cols4all"))),
  access_date = json_escape(access_date),
  scoring_note = json_escape("Scores are computed by loading AI Skills palettes into cols4all runtime data and calling c4a_scores."),
  palettes = paste0("[", paste(objects, collapse = ","), "]")
))

dir.create(dirname(out_path), recursive = TRUE, showWarnings = FALSE)
writeLines(doc, out_path, useBytes = TRUE)
cat("wrote", out_path, "with", length(objects), "palette evaluations\n")
