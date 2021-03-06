"""
Python mapping for the HIServices framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
import sys

import Cocoa
import objc
from HIServices import _metadata, _HIServices

sys.modules["HIServices"] = mod = objc.ObjCLazyModule(
    "HIServices",
    "com.apple.ApplicationServices",
    objc.pathForFramework("/System/Library/Frameworks/ApplicationServices.framework"),
    _metadata.__dict__,
    None,
    {
        "__doc__": __doc__,
        "__path__": __path__,
        "__loader__": globals().get("__loader__", None),
        "objc": objc,
    },
    (
        _HIServices,
        Cocoa,
    ),
)


del sys.modules["HIServices._metadata"]
