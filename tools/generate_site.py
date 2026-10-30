#!/usr/bin/env python3
"""Generate the GitHub Pages site (docs/) from the course repository.

Scans WeekNN folders and the Project folder and emits Jekyll Markdown pages:
class home, per-week pages, per-notebook pages, a notebook index, the project
page, and an about/syllabus page. Notebooks are linked (GitHub / nbviewer /
Colab / download) rather than converted to HTML.

Run from anywhere:  python tools/generate_site.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = "menonpg/BIOENG1340-2026"
BRANCH = "main"
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
NB_DIR = DOCS / "notebooks"

GH_BLOB = f"https://github.com/{REPO}/blob/{BRANCH}"
GH_TREE = f"https://github.com/{REPO}/tree/{BRANCH}"
NBVIEWER = f"https://nbviewer.org/github/{REPO}/blob/{BRANCH}"
COLAB = f"https://colab.research.google.com/github/{REPO}/blob/{BRANCH}"
RAW = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}"

INSTRUCTOR = "Prahlad Menon, PhD, PMP"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def clean_inline(text: str) -> str:
    """Make a markdown snippet safe/readable for an index (drop math + images)."""
    text = re.sub(r"\$\$?.*?\$\$?", "", text)          # drop $...$ / $$...$$
    text = re.sub(r"\\[a-zA-Z]+", "", text)            # drop \command
    text = text.replace("`", "").replace("\\", "")
    return re.sub(r"\s+", " ", text).strip()


def first_paragraph(md: str) -> str:
    """First prose paragraph of a markdown document (skip headings/tables/quotes)."""
    para: list[str] = []
    bullet = re.compile(r"^(#|\||>|!\[|[-*+]\s|\d+\.\s)")
    for line in md.splitlines():
        s = line.strip()
        if not s:
            if para:
                break
            continue
        if bullet.match(s):
            if para:
                break
            continue
        para.append(s)
    return clean_inline(" ".join(para))


def notebook_info(path: Path) -> tuple[str, str]:
    """(title, description) from a notebook's first markdown cell."""
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return path.stem.replace("_", " "), ""
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "markdown":
            src = "".join(cell.get("source", []))
            lines = src.splitlines()
            title = next((l.lstrip("#").strip() for l in lines if l.lstrip().startswith("#")), None)
            body = "\n".join(l for l in lines if not l.lstrip().startswith("#"))
            return title or path.stem.replace("_", " "), first_paragraph(body)
    return path.stem.replace("_", " "), ""


def count_code_cells(path: Path) -> int:
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
        return sum(1 for c in nb.get("cells", []) if c.get("cell_type") == "code")
    except Exception:
        return 0


def readme_title_summary(folder: Path) -> tuple[str, str]:
    readme = folder / "README.md"
    if not readme.exists():
        return folder.name, ""
    md = readme.read_text(encoding="utf-8")
    heading = next((l.lstrip("#").strip() for l in md.splitlines() if l.startswith("# ")), folder.name)
    return heading, first_paragraph(md)


def fm(title: str, **extra) -> str:
    lines = ["---", f'title: "{title}"']
    for k, v in extra.items():
        lines.append(f"{k}: {v}")
    lines += ["---", ""]
    return "\n".join(lines)


def nb_links(rel_path: str) -> str:
    return (
        f"[View on GitHub]({GH_BLOB}/{rel_path}) · "
        f"[nbviewer]({NBVIEWER}/{rel_path}) · "
        f"[Open in Colab]({COLAB}/{rel_path}) · "
        f"[Download]({RAW}/{rel_path})"
    )


def main() -> None:
    NB_DIR.mkdir(parents=True, exist_ok=True)
    weeks = sorted(p for p in ROOT.glob("Week*") if p.is_dir())

    week_rows: list[str] = []
    all_nb: list[tuple[str, str, str, str]] = []   # (week, title, page_slug, rel_path)

    for wk in weeks:
        wtitle, wsummary = readme_title_summary(wk)
        notebooks = sorted(wk.glob("*.ipynb"))
        wk_slug = wk.name.lower()

        # --- per-week page ---
        page = [fm(wtitle, nav_order=wk.name)]
        page.append(f"{wsummary}\n" if wsummary else "")
        page.append(f"[Browse this week on GitHub]({GH_TREE}/{wk.name})\n")
        if notebooks:
            page.append("## Notebooks\n")
            for nb in notebooks:
                ntitle, ndesc = notebook_info(nb)
                nslug = f"{wk_slug}-{slugify(nb.stem)}"
                rel = f"{wk.name}/{nb.name}"
                page.append(f"### [{ntitle}](notebooks/{nslug}.md)\n")
                if ndesc:
                    page.append(f"{ndesc}\n")
                page.append(f"{nb_links(rel)}\n")
                all_nb.append((wk.name, ntitle, nslug, rel))

                # --- per-notebook page ---
                npage = [fm(ntitle, week=wk.name)]
                npage.append(f"*{wk.name} · {count_code_cells(nb)} code cells*\n")
                if ndesc:
                    npage.append(f"{ndesc}\n")
                npage.append("## Open this notebook\n")
                npage.append(f"- [View on GitHub]({GH_BLOB}/{rel}) — rendered with outputs")
                npage.append(f"- [Open in nbviewer]({NBVIEWER}/{rel}) — clean static render")
                npage.append(f"- [Open in Google Colab]({COLAB}/{rel}) — run it in the browser")
                npage.append(f"- [Download .ipynb]({RAW}/{rel})\n")
                npage.append(f"[← {wtitle}]({wk_slug}.md) · [All notebooks](notebooks.md) · [Home](index.md)\n")
                (NB_DIR / f"{nslug}.md").write_text("\n".join(npage), encoding="utf-8")

        page.append("\n[← Home](index.md)\n")
        (DOCS / f"{wk_slug}.md").write_text("\n".join(page), encoding="utf-8")

        topic = wtitle.split("—", 1)[-1].strip() if "—" in wtitle else wtitle
        week_rows.append(f"| [{wk.name}]({wk_slug}.md) | {topic} | {len(notebooks)} |")

    # --- notebooks index ---
    nbindex = [fm("All Notebooks"), "Every runnable notebook in the course, grouped by week.\n"]
    cur = None
    for week, title, slug, rel in all_nb:
        if week != cur:
            nbindex.append(f"\n### [{week}]({week.lower()}.md)\n")
            cur = week
        nbindex.append(f"- [{title}](notebooks/{slug}.md) — "
                       f"[GitHub]({GH_BLOB}/{rel}) · [nbviewer]({NBVIEWER}/{rel}) · [Colab]({COLAB}/{rel})")
    nbindex.append("\n[← Home](index.md)\n")
    (DOCS / "notebooks.md").write_text("\n".join(nbindex), encoding="utf-8")

    # --- home ---
    main_title, main_summary = readme_title_summary(ROOT)
    home = [fm(main_title)]
    home.append(f"{main_summary}\n" if main_summary else "")
    home.append(f"**Instructor:** {INSTRUCTOR}\n")
    home.append("## Weeks\n")
    home.append("| Week | Topic | Notebooks |")
    home.append("|------|-------|-----------|")
    home.extend(week_rows)
    home.append("\n## Explore\n")
    home.append("- [All notebooks](notebooks.md) — the full runnable index")
    home.append("- [Team project](project.md) — framework, datasets, and topic discussions")
    home.append("- [About / syllabus](about.md) — overview and tools")
    home.append(f"\n[View the repository on GitHub](https://github.com/{REPO})\n")
    (DOCS / "index.md").write_text("\n".join(home), encoding="utf-8")

    # --- project ---
    proj_md = (ROOT / "Project" / "README.md").read_text(encoding="utf-8")
    proj_body = "\n".join(l for l in proj_md.splitlines() if not l.startswith("# "))
    proj = [fm("Team Project"), proj_body.strip(),
            f"\n[Browse the project folder on GitHub]({GH_TREE}/Project)\n", "[← Home](index.md)\n"]
    (DOCS / "project.md").write_text("\n".join(proj), encoding="utf-8")

    # --- about ---
    about = [fm("About / Syllabus")]
    about.append(main_summary + "\n")
    about.append(f"**Instructor:** {INSTRUCTOR}\n")
    about.append("## Course arc\n")
    for wk in weeks:
        wtitle, _ = readme_title_summary(wk)
        topic = wtitle.split("—", 1)[-1].strip() if "—" in wtitle else wtitle
        about.append(f"- **{wk.name}** — {topic}")
    about.append("\n## Tools\n")
    about.append("- **Python** (NumPy, SciPy, scikit-image, SimpleITK, matplotlib) in Jupyter notebooks")
    about.append("- **MATLAB** for DICOM I/O, filtering, and VTK export")
    about.append("- **ITK-SNAP** (segmentation) and **ParaView** (3-D visualization)")
    about.append(f"\n[View the repository on GitHub](https://github.com/{REPO})\n")
    about.append("[← Home](index.md)\n")
    (DOCS / "about.md").write_text("\n".join(about), encoding="utf-8")

    print(f"Generated {len(weeks)} week pages, {len(all_nb)} notebook pages, plus home/project/about.")


if __name__ == "__main__":
    main()
