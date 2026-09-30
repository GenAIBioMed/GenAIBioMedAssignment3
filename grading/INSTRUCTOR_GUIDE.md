# Instructor scoring guide (100 points)

This working guide is outside the MkDocs `docs/` directory and does not appear in the student site's navigation. The [student rubric](../docs/grading_rubric.md) gives checkpoint totals and the evidence students should submit.

Score each subitem independently. Award 0 when its evidence is missing or cannot be checked. Use the stated partial-credit conditions for incomplete evidence; otherwise award the listed points only when the result, method, and interpretation are scientifically defensible. Do not impose an extra penalty for the same error. A justified negative or inconclusive result can receive full credit.

## Task 1: Protein mutation analysis (25)

The graded inputs are EGFR (UniProt P00533) variants G719S, T790M, and L858R in canonical numbering. Students start from 4HJO; check that they account for its chain-A numbering offset and engineered V948R construct rather than treating the deposited residue labels as canonical positions.

### P1. Source and residue mapping (5)

- 1: Protein name, accession, and sequence source/version.
- 1: Every candidate uses clear residue notation, with the stated wild-type amino acid checked against the sequence.
- 1: Structure/model ID, chain, source, coverage, and a reliability indicator.
- 2: All candidate positions mapped from sequence to structure/model numbering, including unresolved or mismatched positions; 1 if at least half are mapped correctly.

### P2. Structural or justified alternative evidence (7)

- 2: Reproducible measurement definition: atoms/residues, functional feature or contact rule, units, and structure/model; 1 if one element is missing.
- 3: Valid measurement or documented alternative for every candidate; 2 for at least half, 1 for at least one. An alternative must explain why coordinates are unsuitable and show substitute evidence.
- 2: Candidate-specific limitations of the structural comparison, including missing residues, confidence, ligand presence, or non-equivalent structures where relevant; 1 for limitations discussed only generally.

### P3. Mechanism, evidence, and uncertainty (8)

- 2: Relevant functional annotation or primary literature connected to candidate positions; 1 for a traceable source without a position-specific connection.
- 3: Evidence-grounded mechanism for every candidate; 2 for at least half, 1 for at least one.
- 2: Candidate comparison or ranking with candidate-specific uncertainty; 1 if only the comparison or only uncertainty is present.
- 1: Clear distinction between measured observation, mechanistic prediction, and retrieved external evidence.

### P4. Communication artifacts (5)

- 3: Legible EGFR figure with all three variants and a relevant domain, ligand, or functional site; 2 if only some candidates are marked, 1 for an unlabeled real structure.
- 2: One table covering all candidates with context, evidence, proposed effect, and confidence; 1 if candidates or two required columns are missing.

## Task 2: Single-cell analysis (25)

### S1. Reproducible baseline (6)

- 2: Before/after cell and gene counts, QC metrics/thresholds, and rationale; 1 for counts or thresholds alone.
- 2: Normalization, highly variable genes, PCA, neighbor graph, clustering settings, and seed; 1 if at least four of these six are recorded.
- 1: Cells per baseline cluster.
- 1: Legible UMAP colored by baseline cluster ID.

### S2. Marker-supported annotation (7)

- 3: Marker evidence computed from the student's PBMC3k data for every major cluster; 2 for most, 1 for at least one.
- 3: Major labels supported by observed markers and traceable biological references; 2 for most, 1 for one. An explicit unresolved label is acceptable.
- 1: Code/methods show predefined labels were not used to create annotations.

### S3. Resolution robustness (5)

- 2: At least three Leiden resolutions with other preprocessing and neighbor settings fixed; 1 for exactly two.
- 2: Quantitative correspondence between partitions plus identified splits/merges; 1 for cluster counts alone.
- 1: Biological annotations that remain stable or change are connected to the comparison.

### S4. Downsampling robustness (4)

- 2: Fixed-seed 60–80% cell sample with relevant baseline steps rerun; 1 if sampled without rerunning.
- 1: Quantitative comparison on cells retained in both runs.
- 1: Marker-supported annotations assessed for stability.

### S5. Ambiguous population (3)

- 1: One ambiguous or unstable population identified with evidence.
- 1: Its markers/expression compared with at least one plausible neighboring identity.
- 1: Plausible biological or technical explanation plus a stated unresolved point.

## Task 3: Spatial transcriptomics (25)

### T1. Expression-only domains (5)

- 2: Inspectable code/methods exclude spatial coordinates and tissue annotations from expression feature selection, neighbors, and clustering; 1 if exclusion is only asserted.
- 1: Expression preprocessing, clustering settings, and spot counts per domain.
- 2: Same expression-derived labels in expression space and tissue space with a consistent legend; 1 for tissue projection alone.

### T2. Quantitative spatial organization (5)

- 2: Spatial graph definition includes coordinate system, radius or neighbor count, and off-tissue handling; 1 if only the statistic is named.
- 2: Numerical spatial statistic with interpretation of its direction; 1 for a number without interpretation.
- 1: Statistic connected to the spatial map without claiming a mechanism from coherence alone.

### T3. Spatially variable genes (4)

- 1: Candidate gene set and selection rule, or justified alternative to a laptop-scale set.
- 2: Named method and ranked numerical results with significance or multiple-testing treatment where available; 1 for ranking without numerical details.
- 1: Tissue maps for at least two selected genes.

### T4. Differential-expression comparison (4)

- 2: Named DE method and DE/spatial rankings compared for the same candidate gene set; 1 if gene sets are not aligned.
- 1: Examples of high-both, DE-high/spatial-low, and spatial-high/DE-low, or evidence that a category has no defensible example.
- 1: Explanation of what each ranking measures using those examples.

### T5. Randomized negative control (7)

- 2: Valid null that breaks the tested spatial relationship while preserving relevant counts/values and graph consistency; same statistic in observed and null runs; 1 if preservation or consistency is unclear.
- 1: At least 100 randomizations with seed and count reported.
- 2: Observed statistic shown against a null distribution (plot or center/spread); 1 for one randomized result alone.
- 1: Empirical one-sided tail proportion with justified tail direction.
- 1: Conclusion about non-random organization and a limitation of the control.

## Agent Audit (15)

Score separately for each of the three tasks (5 each): data/software/databases/literature with identifiers (1); computed versus retrieved information (1); independent verification with check and result (2, or 1 for a concrete check without its result); weakness or limitation and how it was evaluated (1).

## Reproducibility and report (10)

- 2: Code/notebooks for all three tasks and README run order; 1 if order is unclear or one task is missing.
- 2: Software versions/environment and data accessions or URLs for all tasks; 1 if only one kind of provenance is complete.
- 2: Parameters and seeds needed for reported comparisons and null controls; 1 if only some tasks are covered.
- 2: Numbered/captioned figures and tables tied to major claims; 1 if artifacts exist but links to claims are incomplete.
- 2: Readable `report.pdf` with all analyses, all three Agent Audits, and checkpoint evidence locator; 1 if the locator or one audit is missing.
