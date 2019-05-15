# -*- coding: utf-8 -*-
#
import os
import sys

# refer to https://github.com/rtfd/sphinx_rtd_theme
# and to https://sphinx-rtd-theme.readthedocs.io/en/stable/
# for original versions

# add paths relative to this conf.py file to directories that include files to be processed &
# added to documentation based on docstrings within modules
sys.path.insert(0, os.path.abspath('../../'))  # root directory of repository
sys.path.insert(0, os.path.abspath('../../docs/source/_demo/_test_module'))  # path for demo test.py file


# -- Project information -----------------------------------------------------

project = 'Sphinx RTD Template'
copyright = '2019, Agent666'
author = 'Agent666'

# The short X.Y version
version = '1.000'
# The full version, including alpha/beta/rc tags
release = '1.000'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'cloud_sptheme.ext.table_styling',
]
# note to install cloud sphinx theme run 'pip install cloud_sptheme', this is required for extended support of tables
# see https://cloud-sptheme.readthedocs.io/en/latest/lib/cloud_sptheme.ext.table_styling.html

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'


# custom css
def setup(app):
    app.add_stylesheet('css/custom.css')


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'sticky_navigation': False,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': False,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
html_theme = 'sphinx_rtd_theme'