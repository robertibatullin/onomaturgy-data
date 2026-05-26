"""Bundled CSV corpora for the onomaturgy name generator.

Exposes :data:`data_path` — the absolute path to the ``csv/`` directory
containing all corpus files.  Used by :mod:`helpers.data_manager` as a
fast local alternative to downloading files from the internet.
"""

import os

data_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'csv')
