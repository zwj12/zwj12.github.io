---
layout: post
title: "Docstring"
date: 2023-12-10 12:54:00 +0800
author: Michael
categories: Python
---

# PEP 257 – Docstring Conventions

[Link](https://peps.python.org/pep-0257/)

# One-line Docstrings
    def kos_root():
        """Return the pathname of the KOS root directory."""
        global _kos_root
        if _kos_root: return _kos_root
        ...

# Multi-line Docstrings
    def complex(real=0.0, imag=0.0):
        """Form a complex number.

        Keyword arguments:
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)
        """
        if imag == 0.0 and real == 0.0:
            return complex_zero
        ...

# module docstring
    """This is the example module.

    This module does stuff.
    """

    from __future__ import barry_as_FLUFL

    __all__ = ['a', 'b', 'c']
    __version__ = '0.1'
    __author__ = 'Cardinal Biggles'

    import os
    import sys