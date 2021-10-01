import os
import re

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import find_packages, setup

base_dir = os.path.dirname(os.path.abspath(__file__))


def get_version(filename="minchin/pelican/plugins/nojekyll.py"):
    with open(os.path.join(base_dir, filename), encoding="utf-8") as initfile:
        for line in initfile.readlines():
            m = re.match("__version__ *= *['\"](.*)['\"]", line)
            if m:
                return m.group(1)


setup(
    name="minchin.pelican.plugins.nojekyll",
    version=get_version(),
    description="Pelican plugin that adds a ``.nojekyll`` file to the output root. Useful for publishing to Github Pages. Written in Python.",
    long_description="\n\n".join([open(os.path.join(base_dir, "README.rst")).read()]),
    long_description_content_type="text/x-rst",
    author="W. Minchin",
    author_email="w_minchin@hotmail.com",
    url="https://github.com/MinchinWeb/minchin.pelican.plugins.nojekyll",
    packages=find_packages(),
    namespace_packages=[
        "minchin",
        "minchin.pelican",
        "minchin.pelican.plugins",
    ],
    include_package_data=True,
    install_requires=[
        "pelican",
    ],
    # dev requirements include minchin.releaser >= 0.4.2
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Pelican :: Plugins",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
