# -*- coding: utf-8 -*-

import traceback

VERSION = "0.1.1"

try:
    from . import tuic
except ImportError:
    traceback.print_exc()