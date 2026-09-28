"""Render the real Scanpy PBMC68k reduced reference data for the assignment page.

Input: 10x_pbmc68k_reduced.h5ad shipped with Scanpy. This is a 700-cell
reference subset of PBMC68k, not the PBMC3k dataset analyzed by students.

Usage:
    python scripts/render_reference_umap.py INPUT.h5ad docs/images/pbmc-reference-umap.png
"""

from __future__ import annotations

import argparse
from pathlib import Path

import h5py
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


PALETTE = [
    "#3B6F9C", "#43A89B", "#77964B", "#D58148", "#815DA0",
    "#B65C78", "#4E8790", "#89929E", "#B89D4B", "#705F94",
]
DISPLAY_NAMES = [
    "CD4 T regulatory", "Naive CD4 T", "Memory CD4 T",
    "Cytotoxic CD8 T", "Naive CD8 T", "CD14 monocytes",
    "CD19 B cells", "CD34 cells", "CD56 NK cells", "Dendritic cells",
]
SOURCE_NAMES = [
    "CD4+/CD25 T Reg", "CD4+/CD45RA+/CD25- Naive T",
    "CD4+/CD45RO+ Memory", "CD8+ Cytotoxic T",
    "CD8+/CD45RA+ Naive Cytotoxic", "CD14+ Monocyte", "CD19+ B",
    "CD34+", "CD56+ NK", "Dendritic",
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    with h5py.File(args.input) as data:
        coordinates = np.asarray(data["obsm"][:]["X_umap"])
        label_ids = np.asarray(data["obs"][:]["bulk_labels"], dtype=int)
        names = [label.decode() for label in data["uns/bulk_labels_categories"][:]]
        if names != SOURCE_NAMES:
            raise ValueError("Unexpected PBMC68k label set; review the plot labels")

    fig = plt.figure(figsize=(11.2, 6.25), dpi=160, facecolor="#F6F8FB")
    ax = fig.add_axes((0.055, 0.14, 0.61, 0.69), facecolor="white")
    ax.scatter(
        coordinates[:, 0], coordinates[:, 1],
        c=[PALETTE[i] for i in label_ids], s=23, alpha=0.88,
        linewidths=0.35, edgecolors="white", rasterized=True,
    )
    ax.set_xlabel("UMAP 1", fontsize=11, color="#425466", labelpad=12)
    ax.set_ylabel("UMAP 2", fontsize=11, color="#425466", labelpad=12)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_color("#E0E6ED")
        spine.set_linewidth(1)

    fig.text(0.055, 0.94, "PBMC reference · 700 real cells", color="#17324D",
             fontsize=17, fontweight="bold", ha="left", va="top")
    fig.text(0.055, 0.895, "Existing UMAP coordinates and reference labels from Scanpy",
             color="#657587", fontsize=11.5, ha="left", va="top")
    fig.text(0.715, 0.82, "Reference labels", color="#17324D",
             fontsize=12, fontweight="bold", ha="left")

    handles = [
        Line2D([0], [0], marker="o", linestyle="", markersize=8,
               markerfacecolor=PALETTE[i], markeredgecolor="none",
               label=f"{DISPLAY_NAMES[i]}  ·  {(label_ids == i).sum()}")
        for i, name in enumerate(names)
    ]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.705, 0.77),
               frameon=False, fontsize=11, labelspacing=1.0,
               handletextpad=0.8, borderaxespad=0)
    fig.text(0.715, 0.18, "Separate reference dataset\nfor visualization only",
             color="#657587", fontsize=10.5, linespacing=1.6, ha="left")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, dpi=160, facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__ == "__main__":
    main()
