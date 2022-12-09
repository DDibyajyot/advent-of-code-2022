import sys


def main():
    input_text = [line.strip() for line in sys.stdin]

    tail_positions = set()
    directions = {
        "R": 1,
        "L": -1,
        "U": 1j,
        "D": -1j,
    }
    head_position = 0
    tail_position = 0
    tail_positions.add(tail_position)
    positions = [0]*10
    long_tail_positions = set()
    long_tail_positions.add(positions[-1])
    for instruction in input_text:
        data = instruction.split()
        direction = directions[data[0]]
        for idx in range(int(data[1])):
            head_position += direction
            tail_position = update_trailing(head_position, tail_position)
            tail_positions.add(tail_position)

            positions[0] += direction
            for idx_p in range(1, len(positions)):
                positions[idx_p] = update_trailing(
                    positions[idx_p-1], positions[idx_p])
            long_tail_positions.add(positions[-1])
        # print(positions)
    print(f"Pt1: {len(tail_positions)}")
    print(f"Pt2: {len(long_tail_positions)}")


def update_trailing(leader, follower):
    delta = leader - follower
    #print(f"{leader}-{follower} = {delta}")
    if delta in [2, -2, 2j, -2j]:
        # In line
        follower += (delta/2)
    elif delta.real in [1, -1] and delta.imag in [1, -1]:
        # Diagonally next to each other
        return follower
    elif (delta.real == 0 and delta.imag in [1, -1]):
        return follower
    elif (delta.real in [1, -1] and delta.imag == 0):
        return follower
    elif delta == 0j:
        return follower
    else:
        # Step one diagonally
        delta = int((delta.imag/abs(delta.imag)))*1j + \
            int((delta.real/abs(delta.real)))
        follower += delta
    return follower


if __name__ == "__main__":
    main()
