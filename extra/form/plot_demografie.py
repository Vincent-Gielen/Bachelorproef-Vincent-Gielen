from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Final


@dataclass(frozen=True)
class ItemCount:
    label: str
    count: int


# Column titles from the Excel file that we want to analyze
COLUMNS_TO_ANALYZE: Final[list[str]] = [
    "How long have you been working on Mainframes?",
    "What is your experience level with Python (on z/OS)?",
    "What is your experience level with Rexx?",
]

PERSONAL_INFO_COLUMN: Final[str] = (
    "Feel free to share your personal information (name, role, company, ...). This is not mandatory."
)

OUTPUT_FILENAMES: Final[dict[str, str]] = {
    "mainframe_experience": "demografie-mainframe-experience.png",
    "python_experience": "demografie-python-experience.png",
    "rexx_experience": "demografie-rexx-experience.png",
    "personal_info_share": "demografie-personal-info-share.png",
}

# Custom sort order for each field (from smallest/least to largest/most)
SORT_ORDER: Final[dict[str, list[str]]] = {
    "mainframe_experience": [
        "Less than 5 years",
        "Between 5 and 10 years",
        "Between 10 and 25 years",
        "More than 25 years",
    ],
    "python_experience": [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Expert",
    ],
    "rexx_experience": [
        "Beginner",
        "Intermediate",
        "Advanced",
        "Expert",
    ],
    "personal_info_share": [
        "Filled",
        "Empty",
    ],
}


def _read_excel_data() -> dict[str, list[ItemCount]]:
    """Read the Excel file and extract value counts for each column."""
    try:
        import pandas as pd
    except ImportError:
        raise ImportError(
            "pandas is required to read Excel files. "
            "Install it with: pip install pandas openpyxl"
        )

    # Hardcoded path to the Excel file
    excel_path = Path(__file__).resolve().parent / "Rexx vs Python comparative study - success criteria(1-22).xlsx"
    
    if not excel_path.exists():
        raise FileNotFoundError(f"Excel file not found: {excel_path}")
    
    df = pd.read_excel(excel_path)

    data = {}

    # Process each column and include all values from SORT_ORDER, even if count is 0
    section_keys = ["mainframe_experience", "python_experience", "rexx_experience"]
    
    for i, column_name in enumerate(COLUMNS_TO_ANALYZE):
        section_key = section_keys[i]
        
        if column_name in df.columns:
            value_counts = df[column_name].value_counts()
            
            # Get all possible values from SORT_ORDER
            possible_values = SORT_ORDER.get(section_key, [])
            
            # Create ItemCount for each possible value, even if count is 0
            items = []
            for label in possible_values:
                count = int(value_counts.get(label, 0))
                items.append(ItemCount(label, count))
            
            data[section_key] = items
        else:
            print(f"Warning: Column '{column_name}' not found in Excel file")

    # Handle personal information share field separately (filled vs empty)
    if PERSONAL_INFO_COLUMN in df.columns:
        values = df[PERSONAL_INFO_COLUMN]

        # Count filled values (non-null, non-empty after trimming) and empty values
        filled = int(
            values.apply(lambda v: pd.notna(v) and str(v).strip() != "").sum()
        )
        total = int(len(values))
        empty = total - filled

        data["personal_info_share"] = [
            ItemCount("Filled", filled),
            ItemCount("Empty", empty),
        ]
    else:
        print(f"Warning: Column '{PERSONAL_INFO_COLUMN}' not found in Excel file")

    return data


def _sorted_least_to_most(items: list[ItemCount], section_key: str) -> list[ItemCount]:
    """Sort items according to custom sort order for the section."""
    sort_order = SORT_ORDER.get(section_key, [])
    
    if sort_order:
        # Create a mapping of label to sort position
        sort_position = {label: i for i, label in enumerate(sort_order)}
        # Sort by the custom order, with unknown items at the end
        return sorted(items, key=lambda x: (sort_position.get(x.label, len(sort_order)), x.label))
    else:
        # Fallback to default sorting (least to most by count)
        return sorted(items, key=lambda x: (x.count, x.label.lower()))


def _plot_one_section(
    *,
    section_key: str,
    section_title: str,
    items: list[ItemCount],
    out_path: Path,
    dpi: int,
    show: bool,
) -> None:
    """Plot a single demographic section as a horizontal bar chart."""
    import matplotlib.pyplot as plt

    sorted_items = _sorted_least_to_most(items, section_key)
    labels = [it.label for it in sorted_items]
    values = [it.count for it in sorted_items]

    fig_h = max(3.0, 0.45 * len(values) + 1.0)
    fig, ax = plt.subplots(figsize=(12, fig_h))

    # Horizontal bars are easier to read for long labels
    ax.barh(range(len(values)), values, color="steelblue")
    ax.set_yticks(range(len(values)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.invert_yaxis()  # Smallest count at the top

    ax.set_title(section_title, fontsize=12, fontweight="bold")
    ax.set_xlabel("Aantal personen", fontsize=10)

    ax.grid(axis="x", linestyle="--", alpha=0.35)
    fig.tight_layout()
    fig.savefig(out_path, dpi=dpi, bbox_inches="tight")
    if show:
        plt.show()
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze demographic data from Excel and generate bar charts"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parent / "plots",
        help="Where to save generated PNG files (default: plots/)",
    )
    parser.add_argument("--dpi", type=int, default=200, help="Output image DPI.")
    parser.add_argument("--show", action="store_true", help="Display figures while also saving.")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Read data from Excel
    data = _read_excel_data()

    if not data:
        print("Error: No data found in Excel file or columns not recognized")
        return

    # Generate plots
    section_config = {
        "mainframe_experience": "How long have you been working on Mainframes?",
        "python_experience": "What is your experience level with Python (on z/OS)?",
        "rexx_experience": "What is your experience level with Rexx?",
        "personal_info_share": "Personal info shared (filled vs empty)",
    }

    for section_key, title in section_config.items():
        if section_key in data:
            out_path = args.output_dir / OUTPUT_FILENAMES[section_key]
            _plot_one_section(
                section_key=section_key,
                section_title=title,
                items=data[section_key],
                out_path=out_path,
                dpi=args.dpi,
                show=args.show,
            )

    print(f"Generated demographic bar charts in: {args.output_dir}")


if __name__ == "__main__":
    main()
