import sys

def main():
    # read in the file
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # initialize the list of lists
    lists = [[]]

    # for each line
    for line in lines:
        # if the line is blank
        if line == '\n':
            # add a new list to the list of lists
            lists.append([])
        # otherwise
        else:
            # add the line to the last list in the list of lists
            lists[-1].append(int(line))

    # initialize the max calories
    max_calories = 0

    # for each list
    for l in lists:
        # if the sum of the list is greater than the max calories
        if sum(l) > max_calories:
            # set the max calories to the sum of the list
            max_calories = sum(l)

    # print the max calories
    print(max_calories)


    # //FOR PART TWO// 

    # now we need to find the sum of the top three max calories
    # initialize the list of max calories
    max_calories = []

    # for each list
    for l in lists:
        # add the max calories to the list of max calories
        max_calories.append(max(l))

    # sort the list of max calories
    max_calories.sort()

    # print the sum of the top three max calories
    print(sum(max_calories[-3:]))
    


if __name__ == '__main__':
    main()