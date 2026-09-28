# GenAIBioMedAssignment3

MkDocs site for the science-agent computational biology assignment.

- [Assignment and checkpoints](docs/index.md)
- [100-point grading rubric](docs/grading_rubric.md)
- [Figure sources and usage notes](docs/figure_sources.md)

To preview the site locally:

```bash
python -m pip install mkdocs mkdocs-material
mkdocs serve
```

Run `mkdocs build --strict` before publishing. The PBMC reference image can be regenerated with `scripts/render_reference_umap.py` using the `10x_pbmc68k_reduced.h5ad` dataset distributed with Scanpy. All figures are credited on the figure-sources page. The assignment input files, extraction commands, and checksums are in [`datasets/README.md`](datasets/README.md).
