---
title: "Workload-driven Predictive Optimization of Lakehouse Table Parameters"
authors: ["Venkata Vamsikrishna Meduri", "David Kreismann", "Berthold Reinwald", "Ronald J. Barber"]
category: patents
date: 2026-01-01
venue: 'IBM'
citation: 'Venkata Vamsikrishna Meduri, <b>David Kreismann</b>, Berthold Reinwald, Ronald J. Barber. (2026). &quot;Workload-driven Predictive Optimization of Lakehouse Table Parameters.&quot; Patent.'
permalink: /de/publications/2026-patent-lakehouse-table-parameters/
translation: /publication/2026-patent-lakehouse-table-parameters
lang: de
share: true
description: "Patent zur automatischen Optimierung von Tabellenparametern in Lakehouse-Systemen anhand der Abfragelast."
---

Dieses Patent beschreibt den Ansatz hinter unserem SIGMOD-2026-Paper [PTO: A Workload-driven Predictive Table Optimizer for Lakehouse Systems](/de/publications/2026-pto-predictive-table-optimizer/).

Lakehouse-Systeme wie Presto auf Apache Iceberg nutzen Tabellenparameter wie Partitionierungsspalten, Zieldateigröße, Zeilengruppengröße und Sortierstrategie, um beim Lesen irrelevante Daten zu überspringen. Das Verfahren analysiert die Filterbedingungen der Abfragelast, grenzt den Suchraum anhand von Selektivität und Abfragehäufigkeit ein und nutzt Tabellenstichproben mit einem gelernten Modell, um eine geeignete Kombination der Parameter vorherzusagen.
