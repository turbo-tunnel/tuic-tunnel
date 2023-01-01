# -*- coding: utf-8 -*-

import traceback

VERSION = "0.1.0"

try:
    from . import tuic
except ImportError:
    traceback.print_exc()