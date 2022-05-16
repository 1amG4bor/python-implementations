# PyPy
A fast python implementation with a JIT compiler

---

## About:
PyPy comes with a Just-in-Time compiler. It is really fast in running most benchmarks —
including very large and complicated Python applications, not just 10-liners.
PyPy works best is when executing long-running programs where a significant fraction of the time is spent executing Python code.

## Should be aware of when PyPy not help:
-  **Short-running processes:** if it doesn't run for at least a few seconds, then the JIT compiler won't have enough time to warm up.
- If all the time is spent in **run-time libraries** (i.e. in C functions), and not actually running Python code, the JIT compiler will not help.

## Features
- **Speed:** using JIT compiler
    - The compilation can be optimized to the targeted CPU
    - Translated code get cached
- **Memory usage:** memory-heavy programs taking less space than they do in CPython
- **Stackless:** use Stackless Python
    - Support for Stackless and greenlets - [more deatials](https://doc.pypy.org/en/latest/stackless.html)


## Pros & Cons

**Advantages**
- Shorter total time of running (compilation + interpretation)
- Could save memory
- Compatible with most of the python libraries
    - Django, Flask, Numpy, Scipy,…
- Debuggers work as well as in python

**Drawbacks**
- Limited CPU architecture support (see below)
- Not work on all Linux distro
- Support only 2 version of python
    - pypy:     **python-2.7.13**
    - pypy3:    **python-3.6.9**
- Currently the speed is noticeable only on python code
- Startup times can be higher
- C extensions are limited and need to be recompiled for PyPy


## How to run
- You need to download and install
    - Go to  ["Downloading and Installing PyPy"](https://doc.pypy.org/en/latest/) page for instructions
    - Or download from  [PyPy.org/download](https://www.pypy.org/download.html#)



## Documentation
The official documentation can be found [here](https://doc.pypy.org/en/latest/).

---
---

## Additional Information:
**Supported CPU architectures:** 
- [x86 (IA-32)](http://en.wikipedia.org/wiki/IA-32) and [x86_64](http://en.wikipedia.org/wiki/X86_64)
- [ARM](http://en.wikipedia.org/wiki/ARM) platforms (ARMv6 or ARMv7, with VFPv3)
- [AArch64](http://en.wikipedia.org/wiki/AArch64)
- [PowerPC](https://de.wikipedia.org/wiki/PowerPC) 64bit both little and big endian
- [System Z (s390x)](https://de.wikipedia.org/wiki/System/390)