# -*- coding: utf-8 -*-

import datetime
import sys
import os

sys.path.insert(0,
    os.path.join(
        os.path.dirname(__file__),
        os.path.pardir,
        'lib'))
import truepy as package


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = package.__package__

original_year = 2012
current_year = datetime.date.today().year
if original_year == current_year:
    copyright = u'%d, %s' % (
        current_year,
        package._info.__author__)
else:
    copyright = u'%d-%d, %s' % (
        original_year,
        current_year,
        package._info.__author__)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(str(v) for v in package._info.__version__)
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % package.__package__

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', package.__package__, u'%s Documentation' % package.__package__,
     [package._info.__author__], 1)
]