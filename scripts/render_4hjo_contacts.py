"""Plot example residue-to-ligand distances from bundled RCSB PDB 4HJO.

Run from the repository root: python scripts/render_4hjo_contacts.py
Distances are the minimum Euclidean distance between non-hydrogen atoms in
protein chain A and ligand AQ4. They describe geometry, not mutation effects.
"""

from collections import defaultdict
from math import dist
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
PDB = ROOT / "datasets/protein/4hjo.pdb"
OUTPUT = ROOT / "docs/images/egfr-ligand-distances.png"


def main():
    residues = defaultdict(list)
    ligand = []
    for line in PDB.read_text().splitlines():
        if not line.startswith(("ATOM  ", "HETATM")) or line[21] != "A":
            continue
        if line[76:78].strip() in {"H", "D"}:
            continue
        xyz = tuple(float(line[i : i + 8]) for i in (30, 38, 46))
        if line.startswith("HETATM") and line[17:20] == "AQ4":
            ligand.append(xyz)
        elif line.startswith("ATOM  "):
            label = f"{line[17:20].title()} {line[22:26].strip()}"
            residues[label].append(xyz)

    if not ligand or not residues:
        raise ValueError("Expected chain A and ligand AQ4 in the 4HJO PDB file")

    nearest = sorted(
        (min(dist(atom, lig_atom) for atom in atoms for lig_atom in ligand), label)
        for label, atoms in residues.items()
    )[:12]
    nearest.reverse()
    labels = [label for _, label in nearest]
    values = [distance for distance, _ in nearest]

    fig, ax = plt.subplots(figsize=(8.3, 5.8), dpi=190)
    fig.patch.set_facecolor("#f7f9fc")
    ax.set_facecolor("#f7f9fc")
    ax.hlines(range(len(values)), 0, values, color="#c2cfdb", linewidth=2.6)
    ax.scatter(values, range(len(values)), s=80, color="#137c83", zorder=3)
    for y, value in enumerate(values):
        ax.text(value + 0.10, y, f"{value:.2f}", va="center", fontsize=9.5, color="#163044")
    ax.set_yticks(range(len(labels)), labels)
    ax.set_xlim(0, 4.1)
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.set_xlabel("Minimum heavy-atom distance to ligand AQ4 (Å)", fontsize=10.5, labelpad=11)
    ax.tick_params(axis="both", length=0, labelsize=9.5)
    ax.grid(axis="x", color="#dfe7ee", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)
    fig.suptitle("EGFR 4HJO · measured proximity to erlotinib", x=0.1, ha="left", y=0.98,
                 fontsize=15, weight="bold", color="#17324b")
    ax.set_title("12 nearest modeled residues in chain A · example geometry only", loc="left",
                 fontsize=10.2, color="#597084", pad=15)
    fig.subplots_adjust(left=0.20, right=0.92, top=0.82, bottom=0.15)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(OUTPUT)


if __name__ == "__main__":
    main()
