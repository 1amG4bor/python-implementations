"""
Channels can be used for bidirectional communication between tasklets.
"""
import stackless
import time


def _print_message(channel):
    while True:
        msg, new_line = channel.receive()
        if new_line:
            print(f'\n{msg}')
        else:
            print(msg, end=' ')


# Tasklet that
def _count_up_to(channel, total):
    i = 0
    channel.send(['Counting...', True])
    while i < total:
        i += 1
        time.sleep(0.3)
        channel.send([i, False])
    channel.send(['Done!', True])
    channel.send(['Totally done!', True])


def run_channel_example():
    print('Run two tasklets that are communicating with each other')
    ch = stackless.channel()
    printer = stackless.tasklet(_print_message)(ch)
    counter = stackless.tasklet(_count_up_to)(ch, 10)
    stackless.run()


if __name__ == '__main__':
    run_channel_example()
