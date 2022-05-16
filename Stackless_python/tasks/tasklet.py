"""
Tasklets wrap functions allowing them to be launched as microthreads
"""
import stackless
import time


# Part-1: Simple tasklet running
def _greet(name):
    print(f'Hello, {name}')


def run_simple_tasklet():
    print('Part-1: run simple tasklet with a greeting function')
    greeting_task = stackless.tasklet(_greet)
    greeting_task.setup('User')
    greeting_task.run()
    print()


# Part-2: Bind function for a tasklet
def _simple_print(text):
    print(text)


def run_tasklet_with_bind():
    print("Part-2: run tasklet with binding a function")
    bound_task = stackless.tasklet()
    bound_task.bind(_greet)
    bound_task.setup('Everybody')
    stackless.run()
    bound_task.bind(_simple_print)
    bound_task.setup('Welcome in the Stackless Python tutorial!')
    stackless.run()
    print()


if __name__ == '__main__':
    run_simple_tasklet()
    time.sleep(2)
    run_tasklet_with_bind()
