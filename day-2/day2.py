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

    #//FOR PART TWO//
#     the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.


    # initialize the score
    score2 = 0

# for each line
    for line in lines:
        # split the line into a list
        l = line.split()

       #since A = rock, B = paper, C = scissors and X = lose, Y = draw, Z = win
       #points for rock is 1, paper is 2, scissors is 3
       #points for win is 6, loss is 0, draw is 3

        # if the first letter is A
        if l[0] == 'A':
            if l[1] == 'X':
                score2 += 3
            elif l[1] == 'Y':
                score2 += 4
            elif l[1] == 'Z':
                score2 += 8

        # if the first letter is B
        elif l[0] == 'B':
            if l[1] == 'X':
                score2 += 1
            elif l[1] == 'Y':
               score2 += 5
            elif l[1] == 'Z':
                score2 += 9


        # if the first letter is C
        elif l[0] == 'C':
            if l[1] == 'X':
                score2 += 2
            elif l[1] == 'Y':
                score2 += 6
            elif l[1] == 'Z':
                score2 += 7

    print(score2)

if __name__ == '__main__':
    main()