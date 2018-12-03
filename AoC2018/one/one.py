
from AoC2018.util import util


def change_frequency(frequency, change):
    return frequency + int(change)


def process_changes(lines):
    frequency = 0
    for change in lines:
        frequency = change_frequency(frequency, change)
    return frequency


def find_duplicate(lines):
    frequency = 0
    frequencies = set()  # store every frequency found
    frequencies.add(frequency)
    while True:
        for change in lines:
            frequency = change_frequency(frequency, change)
            if frequency in frequencies:
                return frequency
            frequencies.add(frequency)


@util.run_timer
def main():
    lines = util.get_input_lines('input')
    result = process_changes(lines)
    print(f'first frequency: {result}')
    result = find_duplicate(lines)
    print(f'first duplicate frequency: {result}')


if __name__ == '__main__':
    main()
