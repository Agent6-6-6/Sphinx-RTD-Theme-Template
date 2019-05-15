Welcome to Agent666's Sphinx RTD Theme Template
===============================================



Changes from the standard Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. Added *Sphinx RTD Theme*

#. Added a number of useful built in *Sphinx* extensions

   a. intersphinx
   #. autodoc
   #. mathjax
   #. viewcode
   #. todo
   #. githubpages
   #. napoleon

#. Added reference to use *Pygments* code syntax highlighter (note if you want to modify this theme copy the ``pygments.css`` file into ``../docs/source/html/_static/css`` directory and change any of the values and it will overwrite the default *Pygment* highlighting theme options)

#. Added reference to an additional theme (*Cloud Sphinx Theme*) that provides for better table formatting options (delete the reference to the extension in the Sphinx config file (*conf.py*) if you do not want to install/use this)

#. Sets a number of default html theme options, such as showing the version in the title, adding next/previous buttons top and bottom, etc

#. Changed default *code block* and ``inline code`` fonts to **Inconsolata** and bumped up font size from **12px to 14px** for a clearer/crisper layout via a custom ``layout.html`` file and ``custom.css`` file

#. Changed default *description* fonts to **Inconsolata** and bumped up font size from **14px to 16px** for a clearer layout, via custom ``layout.html`` file and ``custom.css`` file. Where the font size for the descriptions now more closely match the other default font sizes used for the typical body text (its much smaller by default)

#. Changed default max page width from **800px to 1200px** max to better suit displaying both more text and longer code lines via custom ``custom.css`` file (suits 150 characters per line which is my default goto style). This based on the following code style:-

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
   :target: https://github.com/ambv/Black
   :alt: Black Code

**Black Code** style modified to use max 150 characters per line and prefered single quotes using the following settings:-

.. code-block:: javascript
   :caption: Visual Studio Code settings (settings.json)

   "python.formatting.provider": "black",
   "python.formatting.blackArgs": [
      "--line-length=150",
      "--skip-string-normalization",
   ],

Resulting visual changes
^^^^^^^^^^^^^^^^^^^^^^^^
.. image:: /_images/Comparison.png

To Use
^^^^^^
* Copy the ``docs`` folder to your repository

* Modify ``conf.py`` line ``sys.path.insert(0, os.path.abspath('../../')1)`` to the path(s) where modules are stored that you want to be processed on the basis of docstrings within the modules themselves

* Run ``make html`` at the command prompt from within the ``../docs`` directory to build html files

* View the built html files within the ``_build`` directory

* Note if you subsequently modify the ``custom.css`` file then you may need to run ``make clean`` followed by ``make html`` to pickup the css changes

* Review demo files under ``_demo`` directory for examples of formatting, etc. This directory can be removed, and references to it removed from ``index.rst`` file. Note the example content is taken from the official RTD pages, and due to the wider default page width, and the use of the *Sphinx RTD Theme* some of the formatting may look different (for example footnotes, and some of the examples of test wrapping around images). Some of the intentional errors have bene removed so the documents build remotely on https://sphinx-rtd-theme-template.readthedocs.io/en/latest/

Prerequisites
^^^^^^^^^^^^^
* Sphinx - run ``pip install -U Sphinx`` at the command prompt (http://www.sphinx-doc.org)

* Sphinx RTD Theme - run ``pip install sphinx_rtd_theme`` at the command prompt (https://sphinx-rtd-theme.readthedocs.io/en/stable/)

* Pygments Code Syntax Highlighter - run ``pip install Pygments`` at the command prompt (http://pygments.org/)

* Cloud Sphinx Theme - run ``pip install cloud_sptheme`` at the command prompt  (adds more functionality with respect to tables, see https://cloud-sptheme.readthedocs.io/en/latest/lib/cloud_sptheme.ext.table_styling.html)

Support
-------
If you require support or have any feature requests related to the *Sphinx RTD Theme Template* package please feel free to raise an issue on `Github <https://github.com/Agent6-6-6/Sphinx-RTD-Theme-Template/issues>`_.

License
-------

This project is licensed under the MIT license.


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   Test Page <_rst/test>
.. this is how you give the contents a different title to that in the respective rst files


.. the following is demo content intended to showcase some of the features you can invoke in reStructuredText
.. this can be safely deleted or commented out
.. ........................................................................................

.. toctree::
    :maxdepth: 2
    :numbered:
    :caption: Demo Documents

    _demo/structure
    _demo/demo
    _demo/lists_tables
    _demo/api

.. ........................................................................................
