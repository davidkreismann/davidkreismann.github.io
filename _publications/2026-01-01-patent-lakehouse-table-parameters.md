---
title: "Workload-driven Predictive Optimization of Lakehouse Table Parameters"
collection: publications
category: patents
permalink: /publication/2026-patent-lakehouse-table-parameters
excerpt: 'Patent based on the approach behind <a href="/publication/2026-pto-predictive-table-optimizer">PTO (SIGMOD 2026)</a>: automatically choosing partitioning columns, target file size, row group size and sort strategy of lakehouse tables from the filter predicates of the query workload.'
date: 2026-01-01
venue: 'IBM'
citation: 'Venkata Vamsikrishna Meduri, <b>David Kreismann</b>, Berthold Reinwald, Ronald J. Barber. (2026). &quot;Workload-driven Predictive Optimization of Lakehouse Table Parameters.&quot; Patent.'
---

This patent covers the approach behind our SIGMOD 2026 paper [PTO: A Workload-driven Predictive Table Optimizer for Lakehouse Systems](/publication/2026-pto-predictive-table-optimizer).

Lakehouse systems such as Presto on Apache Iceberg rely on table layout parameters (partitioning columns, target file size, row group size and bin-packing or sort strategy) to skip irrelevant data during scans. Instead of requiring users to set these by hand, the method analyzes the filter predicates of the query workload, narrows the search space with heuristics based on scan selectivity and query frequency, and uses table sampling with a learned model to predict the best combination of parameters.
