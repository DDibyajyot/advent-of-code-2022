import sys

def main():
    # open the file
    with open(sys.argv[1]) as f:
        lines = f.readlines()

# initialize the score
    score = 0

# for each line
    for line in lines:
        # split the line into a list
        l = line.split()

       #since A = rock, B = paper, C = scissors and X = rock, Y = paper, Z = scissors
       #points for rock is 1, paper is 2, scissors is 3
       #points for win is 6, loss is 0, draw is 3

        # if the first letter is A
        if l[0] == 'A':
            if l[1] == 'X':
                score += 4
            elif l[1] == 'Y':
                score += 8
            elif l[1] == 'Z':
                score += 3

        # if the first letter is B
        elif l[0] == 'B':
            if l[1] == 'X':
                score += 1
            elif l[1] == 'Y':
               score += 5
            elif l[1] == 'Z':
                score += 9


        # if the first letter is C
        elif l[0] == 'C':
            if l[1] == 'X':
                score += 7
            elif l[1] == 'Y':
                score += 2
            elif l[1] == 'Z':
                score += 6



    # print the score
    print(score)

if __name__ == '__main__':
    main()