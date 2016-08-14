=====
NoJekyll
=====

``NoJekyll`` is a plugin for `Pelican <http://docs.getpelican.com/>`_,
a static site generator written in Python.

``NoJekyll`` creates a *.nojekyll* file in the root of your output directory.
This is useful when you are publishing your site to
`GitHub Pages <https://pages.github.com/>`_ as it keeps your site from being
run through GitHub's defualt Jekyll site generator. This has a side effect
of make your updated site go live faster.


Installation
============

The easiest way to install ``NoJekyll`` is through the use of pip. This
will also install the required dependencies automatically.

.. code-block:: sh

  pip install minchin.pelican.plugins.nojekyll

Then, in your ``pelicanconf.py`` file, add ``NoJekyll`` to your list of
plugins:

.. code-block:: python

  PLUGINS = [
              # ...
              'minchin.pelican.plugins.nojekyll',
              # ...
            ]

And that's it! No further configuration is needed.


Usage
=====

No configuration is needed.

The ``NoJekyll`` plugin will be automatically called next time you generate
your Pelican site.
