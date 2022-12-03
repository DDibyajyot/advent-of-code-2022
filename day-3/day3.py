import sys

def main():

    # open the file
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # initialize the sum of priorities
    sum_of_priorities = 0

    # for each line
    for line in lines:
        # split the line into 2 lists of equal length
        l1 = line[:len(line)//2]
        l2 = line[len(line)//2:]
        #now to find the common item type and add it only once to the sum
        for i in l1:
            if i in l2:
                sum_of_priorities += ord(i) - 96 if i.islower() else ord(i) - 38
                break


    # print the sum of priorities
    print(sum_of_priorities)

    #//FOR PART TWO//

    
    #divide the lines into groups of 3
    groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
    #initialize the sum of priorities
    sum_of_priorities_three = 0
    #for each group
    for group in groups:
        #find the common item type and add it only once to the sum
        for i in group[0]:
            if i in group[1] and i in group[2]:
                sum_of_priorities_three += ord(i) - 96 if i.islower() else ord(i) - 38
                break



    #print the sum of priorities
    print(sum_of_priorities_three)


if __name__ == "__main__":
    main()