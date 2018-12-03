
from AoC2018.util import util


class Claim:
    def __init__(self, claim):
        data = claim.split()
        location = data[2].split(',')
        size = data[3].split('x')
        self.claim_id = data[0][1:]
        self.x = int(location[0])
        self.y = int(location[1][:-1])
        self.x_offset = self.x + int(size[0])
        self.y_offset = self.y + int(size[1])


def apply_rectangle(fabric, claim):
    c = Claim(claim)
    for y in range(c.y, c.y_offset):
        for x in range(c.x, c.x_offset):
            if fabric[y][x] is '.':
                fabric[y][x] = c.claim_id
            else:
                fabric[y][x] = 'X'  # this coordinate is already claimed
    return fabric


def check_intact(fabric, claim):
    c = Claim(claim)
    for y in range(c.y, c.y_offset):
        for x in range(c.x, c.x_offset):
            if fabric[y][x] is 'X':  # overlay found
                return False
    return True


@util.run_timer
def main():
    fabric = [['.'] * 1000 for _ in range(1000)]

    claims = util.get_input_lines('input')

    for claim in claims:
        apply_rectangle(fabric, claim)
    print(f'overlap count: {util.flatten_and_count_char(fabric, "X")}')

    for claim in claims:
        if check_intact(fabric, claim):
            print(f'found intact claim: {claim}')


if __name__ == '__main__':
    main()
