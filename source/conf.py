# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import sys
from pathlib import Path

from sphinx.util import logging

# Add extensions directory to PYTHONPATH
extension_dir = Path("extensions")
sys.path.insert(0, str(extension_dir.absolute()))


_logger = logging.getLogger(__name__)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "کتاب توسعه‌گر اودوو ۱۷"
copyright = "۱۴۰۴, اودونیکس"
author = "اودونیکس"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.graphviz",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "fa"

# -- Options for HTML output -------------------------------------------------
html_logo = "_static/odoonix-logo.png"
html_title = "توسعه‌گر اودوو ۱۷"


# ----------------------------------HTML Theme: book ---------------------------
# Book them is used in this version. See following link for more inforamtion
# NOTE: theme is forked into extension path
# https://sphinx-book-theme.readthedocs.io/
# ------------------------------------------------------------------------------
# html_theme = 'sphinx-book-theme'
# html_theme_path = ['_themes']
# html_theme_options = {
#     "repository_url": "https://github.com/odoonix/odoo-book-development",
#     "use_repository_button": True,
#     "home_page_in_toc": True,
#     "show_navbar_depth": 1,
#     "max_navbar_depth": 2,
#     "collapse_navbar": True,
#     "footer_start": ["footer_start.html"],
#     "footer_end": ["footer_end.html"]
# }
# html_static_path = ['_static']
# html_css_files = ["custom.css"]


# -------------------------------HTML Theme: Classic ---------------------------
# NOTE: theme is forked into extension path
# https://??
# ------------------------------------------------------------------------------

# html_theme = 'classic'
# html_theme_path = ['_themes']

# html_context = {
#     'css_files': [
#         '_static/custom.css',  # برای افزودن استایل سفارشی
#     ],
# }
# html_static_path = ['_static']


# -------------------------------HTML Theme: Classic ---------------------------
# NOTE: theme is forked into extension path
# https://??
# ------------------------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes"]
html_theme_options = {
    "prev_next_buttons_location": "bottom",
    "analytics_id": "G-XXXXXXXXXX",  #  Provided by Google in your dashboard
    "analytics_anonymize_ip": False,
    "logo_only": False,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "white",
    "flyout_display": "hidden",
    "version_selector": True,
    "language_selector": True,
    # Toc options
    "collapse_navigation": True,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "includehidden": True,
    "titles_only": False,
}
html_static_path = ["_static"]
html_css_files = ["rtd/custom.css"]
