"""
$ python AoC2018/01/runner.py
72330
loop count: 144
runtime: 0.04109048843383789
"""

import time

from AoC2018.util import util

day = '01'

t0 = time.time()

input_lines = util.get_input_lines(day)

frequency = 0
frequencies = set()
frequencies.add(frequency)

loop_count = 0
found = False

while not found:
    for drift in input_lines:
        frequency += int(drift)
        if frequency in frequencies:
            found = True
            print(frequency)
            break
        frequencies.add(frequency)
    loop_count += 1

t1 = time.time()
runtime = t1 - t0
print(f'loop count: {loop_count}')
print(f'runtime: {runtime}')
