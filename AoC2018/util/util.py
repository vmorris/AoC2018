import os


def get_input_lines(day):
    path = os.path.join('./AoC2018', day, 'input')
    with open(path, 'r') as f:
        return f.readlines()
