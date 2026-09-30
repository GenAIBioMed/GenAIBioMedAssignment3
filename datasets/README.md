# Assignment datasets

These are small public input files kept in the repository so students can work from the same starting point. Run the extraction commands from the **repository root**. Do not commit extracted copies if you fork the repository.

| File | Original source | SHA-256 |
| --- | --- | --- |
| `pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz` | [10x Genomics PBMC3k filtered gene-barcode matrices](https://cf.10xgenomics.com/samples/cell-exp/1.1.0/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz) | `847d6ebd9a1ec9a768f2be7e40ca42cbfe75ebeb6d76a4c24167041699dc28b5` |
| `visium_mouse_brain/V1_Adult_Mouse_Brain_filtered_feature_bc_matrix.h5` | [10x Genomics V1 Adult Mouse Brain filtered counts](https://cf.10xgenomics.com/samples/spatial-exp/1.1.0/V1_Adult_Mouse_Brain/V1_Adult_Mouse_Brain_filtered_feature_bc_matrix.h5) | `eb78379e02dcf48036abf05b67233e73ecb0d880787feb82f76ff16f6ce01eb3` |
| `visium_mouse_brain/V1_Adult_Mouse_Brain_spatial.tar.gz` | [10x Genomics V1 Adult Mouse Brain spatial files](https://cf.10xgenomics.com/samples/spatial-exp/1.1.0/V1_Adult_Mouse_Brain/V1_Adult_Mouse_Brain_spatial.tar.gz) | `46d6b05ba740f232d6bf4b27b9a8846815851e000985fb878f1364bab04e5bd4` |
| `protein/4hjo.cif.gz` | [RCSB PDB 4HJO](https://files.rcsb.org/download/4hjo.cif.gz) | `391217cffb1e59d83d669653ecbd710d0ee8ca65d5bc147375365b6257a6d81e` |
| `protein/4hjo.pdb` | [RCSB PDB 4HJO PDB format](https://files.rcsb.org/download/4HJO.pdb) | `95b122b5e152e705fcbcb4314be07ce9378c5a64ab3226e06046ca24ca674948` |

The PBMC3k files were released by 10x Genomics for its [3k PBMC example](https://www.10xgenomics.com/datasets/3-k-pbm-cs-from-a-healthy-donor-1-standard-1-0-0). The Visium count matrix and spatial archive must be used together for Task 3. Task 1 uses **EGFR (UniProt P00533), G719S, T790M, and L858R**. The two 4HJO formats contain the same starting structure; the PDB file is used to create the [example distance plot](../scripts/render_4hjo_contacts.py). The variant names use canonical EGFR numbering, which differs from 4HJO chain-A residue labels. [RCSB's usage policy](https://www.rcsb.org/pages/usage-policy) describes the PDB archive's CC0 terms.

## Extract and load

```bash
tar -xzf datasets/pbmc3k/pbmc3k_filtered_gene_bc_matrices.tar.gz -C datasets/pbmc3k
tar -xzf datasets/visium_mouse_brain/V1_Adult_Mouse_Brain_spatial.tar.gz -C datasets/visium_mouse_brain
```

For example, after extraction:

```python
import scanpy as sc
import squidpy as sq

pbmc = sc.read_10x_mtx(
    "datasets/pbmc3k/filtered_gene_bc_matrices/hg19",
    var_names="gene_symbols",
)
visium = sq.read.visium(
    "datasets/visium_mouse_brain",
    counts_file="V1_Adult_Mouse_Brain_filtered_feature_bc_matrix.h5",
)
visium.var_names_make_unique()  # this file contains duplicate gene symbols
```

The Visium object should include spatial coordinates in `visium.obsm["spatial"]` and tissue images in `visium.uns["spatial"]`, as described by the [Squidpy Visium reader](https://squidpy.readthedocs.io/en/stable/api/squidpy.read.visium.html). Treat these files as raw assignment inputs; the reference images on the course page come from separate examples and are not expected outputs for these files.
