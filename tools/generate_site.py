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


def u(path: str) -> str:
    """A final, baseurl-aware site URL resolved by Jekyll at build time."""
    return "{{ '" + path + "' | relative_url }}"


def html_text(s: str) -> str:
    """Plain, HTML-safe text for use inside raw HTML blocks (hero, cards)."""
    s = s.replace("**", "").replace("`", "")
    return s.replace("&", "&amp;")


def backlinks(*pairs: tuple[str, str]) -> str:
    """A styled footer nav bar from (label, site-path) pairs."""
    inner = " \u00b7 ".join(f'<a href="{u(href)}">{label}</a>' for label, href in pairs)
    return f'<p class="backlinks">{inner}</p>'


def nb_links(rel_path: str) -> str:
    return (
        f"[View on GitHub]({GH_BLOB}/{rel_path}) · "
        f"[nbviewer]({NBVIEWER}/{rel_path}) · "
        f"[Open in Colab]({COLAB}/{rel_path}) · "
        f"[Download]({RAW}/{rel_path})"
    )


def main() -> None:
    NB_DIR.mkdir(parents=True, exist_ok=True)
    # Prune previously generated pages so moved/renamed notebooks leave no stale files.
    for f in NB_DIR.glob("*.md"):
        f.unlink()
    for f in DOCS.glob("week*.md"):
        f.unlink()
    weeks = sorted(
        p for p in ROOT.glob("Week*")
        if p.is_dir() and ((p / "README.md").exists() or any(p.glob("*.ipynb")))
    )

    week_meta: list[tuple[str, str, int]] = []       # (Week name, topic, n notebooks)
    all_nb: list[tuple[str, str, str, str]] = []     # (week, title, page_slug, rel_path)

    for wk in weeks:
        wtitle, wsummary = readme_title_summary(wk)
        notebooks = sorted(wk.glob("*.ipynb"))
        wk_slug = wk.name.lower()

        # --- per-week page ---
        page = [fm(wtitle)]
        page.append(f"{wsummary}\n" if wsummary else "")
        page.append(f"[Browse this week on GitHub]({GH_TREE}/{wk.name})\n")
        if notebooks:
            page.append("## Notebooks\n")
            for nb in notebooks:
                ntitle, ndesc = notebook_info(nb)
                nslug = f"{wk_slug}-{slugify(nb.stem)}"
                rel = f"{wk.name}/{nb.name}"
                page.append(f"### [{ntitle}]({u('/notebooks/' + nslug + '/')})\n")
                if ndesc:
                    page.append(f"{ndesc}\n")
                page.append(f"{nb_links(rel)}\n")
                all_nb.append((wk.name, ntitle, nslug, rel))

                # --- per-notebook page ---
                npage = [fm(ntitle, week=wk.name)]
                npage.append(f"*{wk.name} \u00b7 {count_code_cells(nb)} code cells*\n")
                if ndesc:
                    npage.append(f"{ndesc}\n")
                npage.append("## Open this notebook\n")
                npage.append(f"- [View on GitHub]({GH_BLOB}/{rel}) \u2014 rendered with outputs")
                npage.append(f"- [Open in nbviewer]({NBVIEWER}/{rel}) \u2014 clean static render")
                npage.append(f"- [Open in Google Colab]({COLAB}/{rel}) \u2014 run it in the browser")
                npage.append(f"- [Download .ipynb]({RAW}/{rel})\n")
                npage.append(backlinks((f"\u2190 {wk.name}", "/" + wk_slug + "/"),
                                       ("All notebooks", "/notebooks/"), ("Home", "/")))
                (NB_DIR / f"{nslug}.md").write_text("\n".join(npage), encoding="utf-8")

        page.append(backlinks(("\u2190 Home", "/"), ("All notebooks", "/notebooks/")))
        (DOCS / f"{wk_slug}.md").write_text("\n".join(page), encoding="utf-8")

        topic = wtitle.split("\u2014", 1)[-1].strip() if "\u2014" in wtitle else wtitle
        week_meta.append((wk.name, topic, len(notebooks)))

    # --- notebooks index ---
    nbindex = [fm("All Notebooks"), "Every runnable notebook in the course, grouped by week.\n"]
    cur = None
    for week, title, slug, rel in all_nb:
        if week != cur:
            nbindex.append(f"\n### [{week}]({u('/' + week.lower() + '/')})\n")
            cur = week
        nbindex.append(f"- [{title}]({u('/notebooks/' + slug + '/')}) \u2014 "
                       f"[GitHub]({GH_BLOB}/{rel}) \u00b7 [nbviewer]({NBVIEWER}/{rel}) \u00b7 [Colab]({COLAB}/{rel})")
    nbindex.append("\n" + backlinks(("\u2190 Home", "/")))
    (DOCS / "notebooks.md").write_text("\n".join(nbindex), encoding="utf-8")

    # --- home (hero + card grid) ---
    _, main_summary = readme_title_summary(ROOT)
    cards = ['<div class="card-grid">']
    for name, topic, n in week_meta:
        label = f"{name[:4]} {name[4:]}"             # 'Week11' -> 'Week 11'
        plural = "s" if n != 1 else ""
        cards.append(
            f'<a class="card" href="{u("/" + name.lower() + "/")}">'
            f'<span class="card-week">{label}</span>'
            f'<span class="card-topic">{html_text(topic)}</span>'
            f'<span class="card-meta">{n} notebook{plural}</span></a>'
        )
    cards.append('</div>')
    home = [
        fm("Course Home", hero="true"),
        '<section class="hero">',
        '  <p class="eyebrow">BIOENG 1340/2340 \u00b7 University of Pittsburgh \u00b7 Fall 2026</p>',
        '  <h1 class="hero-title">Medical Image Processing &amp; Analysis</h1>',
        f'  <p class="hero-sub">{html_text(main_summary)}</p>',
        f'  <p class="hero-by">Instructor \u00b7 {INSTRUCTOR}</p>',
        '  <div class="hero-cta">',
        f'    <a class="btn btn-primary" href="{u("/notebooks/")}">Explore notebooks \u2192</a>',
        f'    <a class="btn" href="{u("/project/")}">Team project</a>',
        f'    <a class="btn" href="https://github.com/{REPO}">GitHub \u2197</a>',
        '  </div>',
        '</section>',
        '',
        '<h2 class="section-title">Weeks</h2>',
        "\n".join(cards),
        '<div class="explore">',
        f'  <a class="pill" href="{u("/notebooks/")}">All notebooks</a>',
        f'  <a class="pill" href="{u("/project/")}">Team project</a>',
        f'  <a class="pill" href="{u("/about/")}">About / syllabus</a>',
        f'  <a class="pill" href="https://github.com/{REPO}">Repository \u2197</a>',
        '</div>',
    ]
    (DOCS / "index.md").write_text("\n".join(home), encoding="utf-8")

    # --- project ---
    proj_md = (ROOT / "Project" / "README.md").read_text(encoding="utf-8")
    proj_body = "\n".join(l for l in proj_md.splitlines() if not l.startswith("# "))
    proj = [fm("Team Project"), proj_body.strip(),
            f"\n[Browse the project folder on GitHub]({GH_TREE}/Project)\n",
            backlinks(("\u2190 Home", "/"))]
    (DOCS / "project.md").write_text("\n".join(proj), encoding="utf-8")

    # --- about ---
    about = [fm("About / Syllabus")]
    about.append(main_summary + "\n")
    about.append(f"**Instructor:** {INSTRUCTOR}\n")
    about.append("## Course arc\n")
    for wk in weeks:
        wtitle, _ = readme_title_summary(wk)
        topic = wtitle.split("\u2014", 1)[-1].strip() if "\u2014" in wtitle else wtitle
        about.append(f"- **{wk.name}** \u2014 {topic}")
    about.append("\n## Tools\n")
    about.append("- **Python** (NumPy, SciPy, scikit-image, SimpleITK, matplotlib) in Jupyter notebooks")
    about.append("- **MATLAB** for DICOM I/O, filtering, and VTK export")
    about.append("- **ITK-SNAP** (segmentation) and **ParaView** (3-D visualization)")
    about.append(f"\n[View the repository on GitHub](https://github.com/{REPO})\n")
    about.append(backlinks(("\u2190 Home", "/")))
    (DOCS / "about.md").write_text("\n".join(about), encoding="utf-8")

    print(f"Generated {len(weeks)} week pages, {len(all_nb)} notebook pages, plus home/project/about.")


if __name__ == "__main__":
    main()
