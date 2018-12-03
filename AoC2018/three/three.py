

from AoC2018.util import util


def apply_rectangle(fabric, claim):
    # process claim data
    data = claim.split()
    claim_id = data[0][1:]
    location = data[2].split(',')
    size = data[3].split('x')
    from_left = int(location[0])
    from_top = int(location[1][:-1])
    width = int(size[0])
    height = int(size[1])
    # locate and apply rectangle
    for y in range(from_top, height + from_top):
        for x in range(from_left, width + from_left):
            if fabric[y][x] is '.':
                fabric[y][x] = claim_id
            else:
                fabric[y][x] = 'X'  # this coordinate is already claimed
    return fabric


def check_intact(fabric, claim):
    # process claim data
    data = claim.split()
    location = data[2].split(',')
    size = data[3].split('x')
    from_left = int(location[0])
    from_top = int(location[1][:-1])
    width = int(size[0])
    height = int(size[1])
    # see if overlay has occurred
    for y in range(from_top, height + from_top):
        for x in range(from_left, width + from_left):
            if fabric[y][x] is 'X':
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
