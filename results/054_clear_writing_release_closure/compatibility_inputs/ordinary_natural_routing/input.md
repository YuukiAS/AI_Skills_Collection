# Streaming quantile sketch

A streaming quantile sketch estimates quantiles from a stream without storing
all observations. The KLL sketch keeps a hierarchy of compactors; when one level
fills, it randomly drops roughly half of its items and promotes the survivors to
the next level with larger weight. This gives an error bound that decreases as
the sketch capacity increases.

For a stream of length `n`, an implementation may query approximate ranks such
as the median or the 95th percentile. The sketch is mergeable: two sketches
built on disjoint shards can be combined without replaying the original stream.
This property is useful for distributed telemetry.

The source page includes language navigation, a duplicate "edit this page" link,
and a note that the example was generated from a website template. Those details
do not affect the data structure.
