import sys
import time
from random import seed
from random import randint
import sort

params = sys.argv[1:]
use_custom = params and params[0] == '1'
# Custom means: the sorting algorithm is implemented by me (NOT OPTIMIZED FOR PERFORMANCE)
print(f"Code running on '{sys.implementation.name}' with {'custom' if use_custom else 'built-in'} sorting.")
print(50 * '*' + '\n')

seed(time.time())
max_value = 1_000_000

if use_custom:
    size = 300_000

    start = time.perf_counter()
    print(f'Generating {size:,} random numbers with value up to {max_value:,}...')
    nums = [randint(1, max_value) for i in range(size)]
    print('Sorting by custom merge-sort algorithm...')
    sorted = sort.merge_sort(nums)
    print(f'\nCode has run in {time.perf_counter() - start:.6} seconds.\n')
else:
    size = 1_000_000

    start = time.perf_counter()
    print(f'Generating {size:,} random numbers with value up to {max_value:,}...')
    nums = [randint(1, max_value) for i in range(size)]
    nums.sort()
    print(f'Builtin sort has run in {time.perf_counter() - start:.6} seconds.')

"""
See the difference to run the script with pypy3 or default python3

e.g:
>pypy3 main.py 0  # run on pypy with built-in sort
>pypy3 main.py 1  # run on pypy with custom sort
>python3 main.py 0  # run on python with built-in sort
>python3 main.py 1  # run on python with custom sort
"""