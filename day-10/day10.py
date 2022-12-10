import sys

def main():
    #instead of adding 2 per cycle to make the calculation harder, we can just convert every addx to noop+addx and then add 1 per cycle ie addx
    ops = open('input.txt').read().strip().replace('addx', 'noop\n').splitlines()


    x, total_strength, crt = 1, 0, []
    for cycle, op in enumerate(ops):
        if cycle in range(19, 221, 40):
            total_strength += (cycle+1) * x

        if cycle % 40 == 0:
            crt.append('\n')
        crt.append('█' if abs((cycle % 40)-x) < 2 else ' ')

        if op != 'noop':
            x += int(op)

    print('Part 1: ', total_strength, '\nPart 2:', ''.join(crt))

if __name__ == "__main__":
    main()
