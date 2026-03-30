# Copilot instructions for `odoo-book-development`

## Project purpose
- This repository is a **Sphinx documentation project**, not an Odoo runtime codebase.
- The primary goal is to build an **online Odoo 18 development book in Persian**.
- Phase 1 is translating the public English source book from Cybrosys into Persian.
- Phase 2 is expanding that translated base with **Odoonix experience, real project practices, and practical guidance**.
- Treat the source book as a reference baseline; improve clarity when translation alone is not enough.

## Source of truth
- Main reference: `https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/`
- Authoring files live in `source/`.
- Generated output lives in `build/` and `html/` and must not be edited manually.
- Top-level navigation starts in `source/index.rst`.
- Each chapter has its own folder and chapter-level `index.rst` with a local `toctree`.

## Writing rules
- Write explanations, teaching text, and narrative content in **Persian**.
- Keep code, shell commands, XML, Python identifiers, model names, file paths, and technical literals in **English**.
- Write for **beginners**: explain the concept, why it matters, how it works, and where it is used.
- Prefer practical teaching flow: concept -> example -> explanation -> real-world note.
- Do not translate technical identifiers that should remain exactly as used in Odoo.

## Chapter and file structure
- One chapter maps to one folder under `source/`.
- Each section inside a chapter should be a separate `.rst` file.
- Every new section file must be added to that chapter's `index.rst` in the correct order.
- If a new top-level chapter is added, also update the parent `toctree` in `source/index.rst`.
- Example: `source/creating-odoo-modules/adding-models.rst` must also appear in `source/creating-odoo-modules/index.rst`.
- Preserve the source book ordering unless this repository intentionally uses a different structure.

## Media rules
- Store chapter-specific images inside that chapter's `images/` folder.
- Example path: `source/creating-odoo-modules/images/data-model.png`
- Reference images with standard reStructuredText:

```rst
.. image:: images/data-model.png
   :alt: image description
   :align: center
```

- Use clear English filenames for downloaded media.
- Keep image paths relative to the current `.rst` file.

## What to edit
- Edit chapter content under `source/**/*.rst`.
- Update `toctree` entries when adding, removing, or reordering sections.
- If needed, update `source/conf.py` only for real documentation configuration changes.
- Do not hand-edit generated artifacts in `build/` or `html/`.

## Local workflow
- Activate the virtual environment before running Python-based documentation commands.
- Install dependencies from `requirements.txt`.
- Build docs with `make html`.
- Useful commands: `make help`, `make clean`, `make html`.
- Validate rendering after documentation edits whenever possible.

## Sphinx guidance
- The project uses `pydata_sphinx_theme` and Persian RTL layout configured in `source/conf.py`.
- Follow standard reStructuredText and Sphinx conventions for headings, code blocks, links, lists, and images.
- Keep edits focused and avoid reformatting unrelated files.

## Copilot behavior in this repo
- Prefer editing only files under `source/` unless the task is specifically about project configuration.
- When translating, keep the meaning technically correct and natural in Persian.
- When adding original content, prioritize practical Odoo 18 development experience over generic filler.
- If the English source is unclear, rewrite it into better educational Persian instead of translating it word-for-word.
- Keep the book consistent in tone, structure, and terminology across chapters.



