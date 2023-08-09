========
NoJekyll
========

|pypi|

.. |pypi| image:: https://img.shields.io/pypi/v/minchin.pelican.plugins.nojekyll.svg
    :target: https://pypi.python.org/pypi/minchin.pelican.plugins.nojekyll
    :alt: PyPI Version

``NoJekyll`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``NoJekyll`` creates a *.nojekyll* file in the root of your output directory.
This is useful when you are publishing your site to
`GitHub Pages <https://pages.github.com/>`_ as it keeps your site from being
run through GitHub's default Jekyll site generator. This has a side effect
of make your updated site go live faster.


Installation
============

The easiest way to install ``NoJekyll`` is through the use of pip. This
will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.nojekyll

Assuming you are running Pelican v4.5 (or later), the plugin with
auto-activate. And that's it! No further configuration is needed.


Usage
=====

No configuration is needed.

The ``NoJekyll`` plugin will be automatically called next time you generate
your Pelican site.
