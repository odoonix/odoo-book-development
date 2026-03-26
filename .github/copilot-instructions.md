# Copilot instructions for `odoo-book-development`

## Big picture
- This repository is a **Sphinx documentation project** (not an Odoo runtime app).
- Authoring source lives in `source/`; generated output is `build/` and `html/`.
- Navigation is controlled by `source/index.rst` toctrees; chapter folders map to book sections (for example `source/setup-development-environment/`).
- Sphinx config is in `source/conf.py`:
  - Theme: `pydata_sphinx_theme`
  - Language: `fa`
  - RTL context enabled (`html_context = {"rtl": True}`)
  - Custom static assets in `source/_static/` (for example `custom.css`, `odoonix-logo.png`).

## What to edit (and what not to)
- Edit chapter/content files under `source/**/*.rst`.
- Keep section structure consistent with existing `index.rst` + `.. toctree::` patterns.
- Do **not** hand-edit generated artifacts in `build/` or `html/`.
- Keep code snippets, commands, identifiers, and technical comments in English.
- Keep book prose in Persian (existing convention in content files like `source/introduction.rst`).

## Local workflow
- Create/activate a Python virtualenv, then install deps from `requirements.txt`.
- Build docs with `make html` (uses `Makefile` wrapper around `sphinx-build -M`).
- Useful targets from Sphinx make mode: `make help`, `make clean`, `make html`.
- Check build output pages in `html/index.html` after generation.

## CI and quality gates
- CI workflows are in `.github/workflows/` (`pre-commit.yml`, `test.yml`).
- Pre-commit runs `pre-commit run --all-files` and expects no unstaged/generated leftovers.
- Repository includes broad OCA pre-commit hooks in `.pre-commit-config.yaml`; some are addon-oriented and template-derived, so prefer minimal, scoped changes.
- Test workflow also contains OCA addon checks (`oca_install_addons`, `oca_run_tests`), which are not the primary local docs workflow.

## Agent-specific guidance
- When adding a new chapter, update both the chapter `index.rst` and parent toctree entry in `source/index.rst` (or the relevant section index).
- Preserve current style and heading hierarchy used in nearby `.rst` files.
- Keep edits surgical: avoid reformatting unrelated files or touching generated directories.
- If changing theme/static behavior, verify references in `source/conf.py` and `source/_templates/`.
- If unsure whether a file is generated, prefer editing under `source/` only.