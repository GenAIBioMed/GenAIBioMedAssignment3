# Checkpoints and Grading Rubric

The assignment is worth **100 points**: Protein **25**, single-cell **25**, spatial **25**, Agent Audit **15**, and reproducibility/report **10**. Use the checkpoint IDs below to track your progress. In `report.pdf`, add a short evidence index such as `P2 → Figure 2, Table 1, protein/measure.py`.

**How points are awarded:** Full credit requires clear results and enough code or source information to check them. Incomplete but valid evidence earns partial credit; missing or unverifiable evidence earns 0. There is no required biological answer or target statistic. A well-supported negative or uncertain result can earn full credit.

## Task 1: Protein mutation analysis — 25 points

| Checkpoint | Show in your submission | Points |
| --- | --- | ---: |
| **P1 · Map the variants** | Identify the protein, verify each variant against its sequence, and map all candidate residues to the chosen structure/model. | 5 |
| **P2 · Measure structural evidence** | Define and report reproducible measurements for each candidate, or explain and document a justified alternative where coordinates are unavailable. | 7 |
| **P3 · Interpret with evidence** | Compare candidate mechanisms using observed results and cited sources; separate observations from predictions and state uncertainty. | 8 |
| **P4 · Communicate the comparison** | Provide an annotated structure of the assigned protein and one table covering every candidate. | 5 |

## Task 2: Single-cell analysis — 25 points

| Checkpoint | Show in your submission | Points |
| --- | --- | ---: |
| **S1 · Baseline and QC** | Report QC decisions, analysis settings and seed, cluster sizes, and a cluster-labeled UMAP. | 6 |
| **S2 · Cell-type evidence** | Use markers computed from your PBMC3k data and cited biology to support major labels; do not use predefined labels. | 7 |
| **S3 · Resolution check** | Compare at least three Leiden resolutions with other settings fixed; quantify splits/merges and discuss label stability. | 5 |
| **S4 · Downsampling check** | Rerun a fixed-seed 60–80% cell sample; compare retained cells quantitatively and discuss label stability. | 4 |
| **S5 · Ambiguous population** | Investigate one unclear or unstable population with marker comparisons and a reason for the uncertainty. | 3 |

## Task 3: Spatial transcriptomics — 25 points

| Checkpoint | Show in your submission | Points |
| --- | --- | ---: |
| **T1 · Expression-only domains** | Cluster using expression without spatial information; show the same labels in expression space and on tissue, with settings and spot counts. | 5 |
| **T2 · Spatial organization** | Define the physical-neighbor graph and report an interpreted numerical spatial statistic. | 5 |
| **T3 · Spatial genes** | State the tested gene set and method, rank spatially variable genes, and map at least two genes on tissue. | 4 |
| **T4 · Compare gene rankings** | Compare differential-expression and spatial rankings for the same genes, with examples that explain their differences. | 4 |
| **T5 · Negative control** | Use at least 100 fixed-seed randomizations; compare the same observed and null statistic, report an empirical comparison, and note a limitation. | 7 |

## Agent Audit — 15 points

For **each task** (5 points each), show: sources used (1), what the agent computed versus retrieved (1), one independent check **and its result** (2), and one weakness or limitation you evaluated (1).

## Reproducibility and report — 10 points

Two points each for: ordered code/notebooks with a run README; data sources and software versions; settings and random seeds; labeled figures/tables tied to conclusions; and a readable `report.pdf` with all three Agent Audits and the checkpoint evidence index.

Before submitting, mark each checkpoint **complete** or **needs revision** and give the page or file containing its evidence.
