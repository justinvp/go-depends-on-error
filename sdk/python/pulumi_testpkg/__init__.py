# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .provider import *
from .static_page import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "testpkg",
  "mod": "index",
  "fqn": "pulumi_testpkg",
  "classes": {
   "testpkg:index:StaticPage": "StaticPage"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "testpkg",
  "token": "pulumi:providers:testpkg",
  "fqn": "pulumi_testpkg",
  "class": "Provider"
 }
]
"""
)
