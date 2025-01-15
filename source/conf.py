# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
from pathlib import Path
from sphinx.util import logging



# Add extensions directory to PYTHONPATH
extension_dir = Path('extensions')
sys.path.insert(0, str(extension_dir.absolute()))


_logger = logging.getLogger(__name__)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'کتاب توسعه‌گر اودوو ۱۷'
copyright = '۱۴۰۴, اودونیکس'
author = 'اودونیکس'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'fa'

# -- Options for HTML output -------------------------------------------------
# Book them is used in this version. See following link for more inforamtion
# NOTE: theme is forked into extension path
# https://sphinx-book-theme.readthedocs.io/
html_theme = 'sphinx_book_theme'
html_theme_path = ['_themes']
html_theme_options = {
    "repository_url": "https://github.com/odoonix/odoo-book-development",
    "use_repository_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 1,
    "max_navbar_depth": 2,
    "collapse_navbar": True,
    "footer_start": ["footer_start.html"],
    "footer_end": ["footer_end.html"]
}
html_logo = "_static/odoonix-logo.png"
html_title = "توسعه‌گر اودوو ۱۷"
html_static_path = ['_static']
html_css_files = ["custom.css"]
