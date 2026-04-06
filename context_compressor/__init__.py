"""
context-compressor - Compress context efficiently without losing data

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ContextCompressor, compress, process, main

__all__ = ["ContextCompressor", "compress", "process", "main"]
