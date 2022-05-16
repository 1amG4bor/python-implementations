# Python implementations

An "implementation" of Python should be taken to mean a program or environment which provides support for the 
execution of programs written in the Python language.<br>
The default/de-facto implementation of python is the CPython but there are other existing variants of it
furthermore some additional working implementations that have advantages as well as drawbacks against the CPython.

####  Implementations
- [MicroPython](https://micropython.org/) - Python for microcontrollers (runs on the pyboard and the BBC Microbit)
- **[PyPy](https://pypy.org/)** - Python in Python, A fast python implementation with a JIT compiler
- **[Jython](http://www.jython.org/)** - Python in Java for the Java platform, Python running on the Java Virtual
 Machine
- [IronPython](http://ironpython.net/) - Python in C# for the Common Language Runtime (CLR/.NET) and the FePy project's IronPython Community
 Edition (IPCE)
- **[Stackless Python](http://www.stackless.com/)** - CPython with an emphasis on concurrency using tasklets and
 channels 

[Full list of Python implementations](https://wiki.python.org/moin/PythonImplementations)

---

The aim of this project is to show how to use certain implementations and reap their benefits.<br>
Since there are quite a few of them, I will show only a few.

#### Examples
1. [Jython demo](./Jython/ReadMe.md) - presents two varieties of usage of this implementation. 
    1. When we use python code in our Java application
    2. When we use Java code in our Python script

2. [PyPy demo](./PyPy/ReadMe.md) - shows the advantage of PyPy in performance for computation heavy processes 

3. [Stackless Python demo](./Stackless_python/ReadMe.md) - is a simple example of concurrent calculation in Python
