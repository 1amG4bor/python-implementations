from tasks import tasklet, scheduler, channel, exception


# Helper functions
def print_header(text):
    print(f'{6*"#"} {text} {6*"#"}')


def separator():
    print(f'\n{21*"*"}\n')


# Simple 'Tasklet'
print()
print_header('Tasklet(s): wrap functions allowing them to be launched as microthreads')
tasklet.run_simple_tasklet()
tasklet.run_tasklet_with_bind()

separator()
# Using the 'Scheduler'
print_header('Schedulers can be used to schedule tasklets either cooperatively or preemptively')
scheduler.run_scheduler()
scheduler.run_preemptive_counter()

separator()
# Communication between tasklets via 'Channel'
print_header('Channels can be used for bidirectional communication between tasklets')
channel.run_channel_example()

separator()
# Exception handling
print_header('Exceptions that occur within tasklets and are uncaught are raised out of the stackless.run() call.')
exception.run_safe_tasklet()
exception.run_tasklet_that_may_throw_an_exception()
