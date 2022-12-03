# "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

# The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

# For example, suppose you were given the following strategy guide:

# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide?

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
            # if the second letter is X
            if l[1] == 'X':
                # add 3+1 to the score
                score += 4
            # if the second letter is Y
            elif l[1] == 'Y':
                # add 6+2 to the score
                score += 8
            # if the second letter is Z
            elif l[1] == 'Z':
                # add 0+3 to the score
                score += 3

        # if the first letter is B
        elif l[0] == 'B':
            # if the second letter is X
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
                score += 9


    # print the score
    print(score)

if __name__ == '__main__':
    main()