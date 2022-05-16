# Stackless Python
Branch of CPython supporting microthreads

---

## About:
Allows to take the advantage of thread-based programming in python. 
Avoid using the C call stack instead its own stack.
Stackless Python uses the C stack, but the stack is cleared between function calls.


## Features

- **Microthreads:** tasklets wrap functions allowing them to be launched as microthreads(not real concurrency)
- **Channels** can be used for bidirectional communication between tasklets
- **Scheduler** is built in. It can be used to schedule tasklets either cooperatively or preemptively
- **Serialization:** tasklets can be serialized to disk through pickling for later resumption of execution.

## Pros & Cons

**Advantages**
- Lightweight
- Has scheduler to manage tasklets
- Support preemptive scheduling
- Communication between tasklets


**Drawbacks**
- Exceptions within tasklets are expected to reach the scheduler (hard to track down issues)
- Debugging is not likely to work

## How to run this script or start working in Stackless:

- You need to download and install stackless
    - Go to  [Stackless-dev (wiki)](https://github.com/stackless-dev/stackless/wiki#downloads) for instructions
    - Or download from  [Stackless-dev: downloads](https://github.com/stackless-dev/stackless/wiki/Download)
- **Config your project to use the interpreter of stackless python instead of the default one** 

## Documentation
The official documentation can be found [here](https://stackless.readthedocs.io/en/3.6-slp/stackless-python.html).