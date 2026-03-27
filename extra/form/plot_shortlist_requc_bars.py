from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Final


@dataclass(frozen=True)
class ItemCount:
    label: str
    count: int


# Hardcoded shortlist counts, ordered exactly as they appear in `shortlist Req&UC.md`.
# The plot function will sort least -> most before drawing.
#
# If you change the shortlist text later, update these values accordingly.
SECTIONS: Final[dict[str, tuple[str, list[ItemCount]]]] = {
    "requirements": (
        "Requirements (Requirements voor PoC)",
        [
            ItemCount("Moet kunnen integreren met tools van Mainframe", 6),
            ItemCount("Moet kunnen integreren met tools buiten Mainframe", 3),
            ItemCount(
                "Ondersteuning van de taal (vendors, community, documentatie, developer tooling)",
                4,
            ),
            ItemCount("Security vulnerabilities", 3),
            ItemCount("Robuustheid (hoe lang gaat de code mee)", 6),
            ItemCount("Herbruikbaarheid van code (libraries, GIT, )", 7),
        ],
    ),
    "use_cases": (
        "Use cases",
        [
            ItemCount("Het werken met z/OS datasets en USS files", 2),
            ItemCount("Gebruik van API's", 4),
            ItemCount(
                "Genereren van JCL m.b.v. ISPF REXX File Tailoring services of Python Jinja templating",
                3,
            ),
            ItemCount("ISPF support", 5),
            ItemCount("Interfacing met MasterConsoles", 1),
            ItemCount("Equivalent van PARSE en ADDRESS in Python", 3),
            ItemCount(
                "Oproepen van services zoals DFSMS, RACF, ZOS, ISPF, SDSF, WLM, DB2, USS, TSO etc.",
                4,
            ),
            ItemCount("Rexx stems vs lists of dict of objects in Python", 2),
            ItemCount("Informatie uit SDSF halen", 1),
            ItemCount("Job submitten en output rapporteren", 1),
            ItemCount("RACF cleanups", 2),
            ItemCount("Opstarten van LPARs", 1),
            ItemCount("Genereren van rapporten", 1),
        ],
    ),
    "dont_do": (
        "Wat we niet doen",
        [
            ItemCount("Performance en CPU gebruik", 3),
            ItemCount("AI/LLM support", 1),
            ItemCount("Rexx EBCDIC vs Python Unicode", 2),
            ItemCount("Voorganger CLIST vs REXX", 1),
            ItemCount("Structuur van de code", 1),
            ItemCount("Object georiënteerd programmeren", 1),
            ItemCount("Steun voor AI/LLM's", 1),
            ItemCount("Lijnen code", 2),
        ],
    ),
    "literature_processing": (
        "Verwerken van de antwoorden uit de form voor literatuur",
        [
            ItemCount("Hoeveelheid mensen die nu en in de toekomst de taal kennen", 7),
            ItemCount(
                "Python is gratis op zIIP, maar niet zo'n hoog volume dat het een groot prijsverschil kan maken",
                2,
            ),
            ItemCount("Geen support voor Rexx", 2),
            ItemCount(
                "Rexx script data te verwerken. Wil herschrijven in Python, maar bedrijf heeft ZOAU nog niet geimplementeerd.",
                1,
            ),
            ItemCount(
                "Wil read/write doen naar USS met Rexx, moest add-on libraries installeren.",
                1,
            ),
            ItemCount("Gebruik van de taal hangt af van de use case.", 5),
            ItemCount(
                "REXX en Python zijn allebei niet het meest geschikt voor zware ladingen of performance kritische toepassingen.",
                1,
            ),
            ItemCount("Rexx wordt gebruikt voor kleine scripts", 2),
            ItemCount(
                "Python wordt voornamelijk gebruikt als er intercatie met de buitenwereld nodig is",
                2,
            ),
            ItemCount(
                "Een extreme blik: Python is andermans packages, Rexx is alles zelf schrijven.",
                1,
            ),
            ItemCount("Mainframe heeft nog problemen met USS support", 2),
        ],
    ),
}

OUTPUT_FILENAMES: Final[dict[str, str]] = {
    "requirements": "shortlist-requirements.png",
    "use_cases": "shortlist-use-cases.png",
    "dont_do": "shortlist-dont-do.png",
    "literature_processing": "shortlist-literature-processing.png",
}


def _sorted_least_to_most(items: list[ItemCount]) -> list[ItemCount]:
    # Least to most, stable for identical counts.
    return sorted(items, key=lambda x: (x.count, x.label.lower()))


def _plot_one_section(
    *,
    section_title: str,
    items: list[ItemCount],
    out_path: Path,
    dpi: int,
    show: bool,
) -> None:
    import matplotlib.pyplot as plt

    sorted_items = _sorted_least_to_most(items)
    labels = [it.label for it in sorted_items]
    values = [it.count for it in sorted_items]

    fig_h = max(3.0, 0.45 * len(values) + 1.0)
    fig, ax = plt.subplots(figsize=(12, fig_h))

    # Horizontal bars are easier to read for long Dutch labels.
    ax.barh(range(len(values)), values)
    ax.set_yticks(range(len(values)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.invert_yaxis()  # so the smallest count is at the top

    ax.set_title(section_title)
    ax.set_xlabel("Aantal keer verschenen")

    ax.grid(axis="x", linestyle="--", alpha=0.35)
    fig.tight_layout()
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate bar charts (least -> most) from hardcoded shortlist counts"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent,
        help="Where to save generated PNG files.",
    )
    parser.add_argument("--dpi", type=int, default=200, help="Output image DPI.")
    parser.add_argument("--show", action="store_true", help="Display figures while also saving.")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Always generate files; optionally show them too.
    for section_key, (title, items) in SECTIONS.items():
        out_path = args.output_dir / OUTPUT_FILENAMES[section_key]
        _plot_one_section(
            section_title=title,
            items=items,
            out_path=out_path,
            dpi=args.dpi,
            show=args.show,
        )

    print(f"Generated bar charts in: {args.output_dir}")


if __name__ == "__main__":
    main()

