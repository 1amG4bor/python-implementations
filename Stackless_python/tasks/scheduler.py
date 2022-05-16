"""
Schedulers can be used to schedule tasklets either cooperatively or preemptively.
- Cooperative: each tasklet to get itself rescheduled so that other tasklets can have a turn
- Preemptive: manage the scheduler to run for only a specific number of instructions per tasklet.
"""
import stackless
import time


# Part-1: Cooperative scheduling: each tasklet to get itself rescheduled so that other tasklets can have a turn.
def _lunch(name, is_male, is_lazy=True):
    print(f'{name} takes out {"his" if is_male else "her"} lunch.')
    stackless.schedule()
    print(f'{name} eating...')
    stackless.schedule()
    print(f'{name} {"is taking a rest." if is_lazy else "do the dishes."}')
    stackless.schedule()


def run_scheduler():
    print('Part-1: run multiple tasklet next to each other with scheduler')
    stackless.tasklet(_lunch)('Sarah', False)
    stackless.tasklet(_lunch)('Dad', True)
    stackless.tasklet(_lunch)('Mom', False, False)
    stackless.run()
    print('***** Cooperative scheduler has finished! *****\n')


# Part-2: Preemptive scheduling: running the tasklets for only a specific number of instructions.
def _count(author, start, end, is_increment):
    inc = 1 if is_increment else -1
    i = start - inc
    while i is not end:
        i += inc
        print(f'Author: {author} - {i}')
        time.sleep(0.01)


def run_preemptive_counter():
    print('Part-2: run preemptive counter tasklet')
    max_instructions = 30

    stackless.tasklet(_count)('Incrementer', 1, 20, True)
    stackless.tasklet(_count)('Reducer', 20, 1, False)

    while stackless.getruncount() != 1:
        tasks = stackless.run(max_instructions)

        # insert back the tasklet(s) to the scheduler if they are not finished
        if tasks is not None:
            tasks.insert()
    print('***** Preemptive counting has finished! *****\n')


if __name__ == '__main__':
    run_scheduler()
    time.sleep(2)
    run_preemptive_counter()
