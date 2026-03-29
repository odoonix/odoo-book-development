# Copilot instructions for `odoo-book-development`

## Big picture
- This repository is a **Sphinx documentation project** (not an Odoo runtime app).
- The main goal is to author and maintain the Odoo Development Book in Persian.
- We use best practices from Odoonix Developers and experiences in real projects to create a comprehensive, accurate, and up-to-date resource.
- Authoring source lives in `source/`; generated output is `build/` and `html/`.
- Navigation is controlled by `source/index.rst` toctrees; chapter folders map to book 
  sections (for example `source/setup-development-environment/`).
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
- Active virtualenv with `source .venv/bin/activate` and then call other commands.
- Build docs with `make html` (uses `Makefile` wrapper around `sphinx-build -M`).
- Useful targets from Sphinx make mode: `make help`, `make clean`, `make html`.
- Check build output pages in `html/index.html` after generation.

## CI and quality gates
- CI workflows are in `.github/workflows/` (`pre-commit.yml`, `static.yml`).
- Pre-commit runs `pre-commit run --all-files` and expects no unstaged/generated leftovers.
- Repository includes sphonix pre-commit hooks in `.pre-commit-config.yaml`.
- The workflow also contains Github Page (`upload-pages-artifact`), which are not the primary local docs workflow.
- All artifacts are loaded to branch `gh-pages`.
- For each branch there is a seperate folder in `gh-pages` branch. For example for `main` branch the folder is `main/` and for `develop` branch the folder is `develop/`. So the documentation for each branch is available in the corresponding folder in `gh-pages` branch.
- main branch documentation is copy to the root repository too.
- Online result are availabel on https://odoonix.github.io/odoo-book-development/ .

## Agent-specific guidance
- When adding a new chapter, update both the chapter `index.rst` and parent toctree entry in `source/index.rst` (or the relevant section index).
- Preserve current style and heading hierarchy used in nearby `.rst` files.
- Keep edits surgical: avoid reformatting unrelated files or touching generated directories.
- If changing theme/static behavior, verify references in `source/conf.py` and `source/_templates/`.
- If unsure whether a file is generated, prefer editing under `source/` only.
- Use `make html` to verify that changes render correctly and do not introduce build errors.
- Use sphonix guildelines for writing reStructuredText (reST) syntax in `.rst` files, especially for code blocks, images, and links.
- Use pydata-sphinx-theme guidline from online document at https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html


## Resources
- The main reference is https://www.cybrosys.com/odoo/odoo-books/odoo-18-development
- We translate from en to fa

here is list of chapters

  introduction
  about/index
  setup-development-environment/index
  creating-odoo-modules/index
  server-side-development/index
  data-management/index
  views/index
  security/index
  internationalization/index
  web-development/index
  website-development/index
  odoo-web-library/index
  test-cases/index
  odoo-sh/index
  remote-procedure-calls-rpc/index
  performance-optimisation/index
  emails/index
  pos/index
  iot-box/index
  others/index
  appendex/index

related to each chapter there is a online document.


https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/about/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/set-up-development-environment/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/creating-odoo-modules/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/server-side-development/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/data-management/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/views/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/security/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/internationalization/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/web-development/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/website-development/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/odoo-web-library/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/test-cases/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/odoo-sh/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/remote-procedure-calls-rpc/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/performance-optimisation/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/emails/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/point-of-sales/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/iot-box/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/others/
https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/conclusion/



## Docuemnt Structure

There are a tree struction

each chapter is linked to a folder by name.

for example the following contetn is a chapter

https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/creating-odoo-modules/

so there is a folder named 

creating-odoo-modules

There is index.rst file in each folder that contains link to all parts with toctree. the
file path is

creating-odoo-modules/index.rst

for each part there is rst file in the chapter folder.

for example

https://www.cybrosys.com/odoo/odoo-books/odoo-18-development/creating-odoo-modules/adding-models


there is a file

  creating-odoo-modules/adding-models.rst


and the adding-models is added to the toc tree in index.rst

.. toctree::
  :maxdepth: 2
  :caption: فهرست مطالب:

  adding-models


به همین ترتیب سایر بخش‌های یک فصل به صورت یک فایل ایجاد شده و در فایل اصلی فصل که همان
index.rst در پوشه مربوط به فصل است اضافه می‌شود. نکته اینکه ترتیب این فصل‌ها و اضافه شدن
در فایل اصلی مهم است.


## Media

تمام تصاویر و مدیاهای که در هر فصل اتفاده می‌شود در یک پوشه خاص به نام images ذخیره باید
شوند.

برای نمونه در پوشه فصل creating-odoo-modules یک پوشه به نام images ایجاد می شود و یک فایل
به نام data-model.png در آن دانلود و ذخیره می‌شود. آدرس فایل به صورت زیر است


creating-odoo-modules/images/data-model.png

بعد در متن این تصویر به صورت زیر استفاده خواهد شد:

.. image:: images/data-model.png
   :alt: image alternative
   :align: center



