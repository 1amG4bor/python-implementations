"""
Exceptions that occur within tasklets and are uncaught are raised out of the stackless.run() call.
These exceptions should be handled by its caller.
"""
import stackless
import time
import random


def _raise_exception():
    while True:
        print("Working...", end=' ')
        time.sleep(1)
        if random.randint(0, 2) == 0:
            raise Exception('Catch me if you can!')
        else:
            print('Done')


def new_tasklet(f, *args, **kwargs):
    def safe_tasklet():
        try:
            f(*args, **kwargs)
        except Exception as err:
            print(f"Error has been detected: '{err}'")
    return stackless.tasklet(safe_tasklet)()


def run_tasklet_that_may_throw_an_exception():
    print('Run tasklet without handling exception')
    stackless.tasklet(_raise_exception)()
    stackless.run()
    print()


def run_safe_tasklet():
    print('Run tasklet that handle exceptions')
    new_tasklet(_raise_exception).run()
    print()


if __name__ == '__main__':
    # run_tasklet_that_may_throw_an_exception()
    run_safe_tasklet()
