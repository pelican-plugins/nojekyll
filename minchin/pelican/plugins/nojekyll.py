# -*- coding: utf-8 -*- #
"""
NoJekyll
========

This plugin for Pelican add a *.nojekyll* file to the output root.
"""

import logging
import os

from pelican import signals

__version__ = "1.2.1-dev"

logger = logging.getLogger(__name__)


def add_nojekyll(p):
    """
    :param p: pelican instance
    :return: None
    """

    nojekyll_path = os.path.join(p.output_path, ".nojekyll")
    content = " "
    with open(nojekyll_path, "w") as f:
        f.write(content)
    logger.info("[noJekyll] written to %s" % nojekyll_path)


def register():
    signals.finalized.connect(add_nojekyll)
