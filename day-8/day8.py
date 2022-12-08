import numpy as np
import sys

def main():
    # Open the file
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # Get the data
    data = [line.strip() for line in lines]

    # Convert the input to a numpy array
    data = np.array([list(line) for line in data])

    # Get the dimensions of the array
    rows, cols = data.shape

    # Create a new array to store the number of trees visible from each cell
    visible = np.zeros((rows, cols), dtype=int)

    #the trees on the edge are visible from all directions
    visible[0, :] = 1
    visible[-1, :] = 1
    visible[:, 0] = 1
    visible[:, -1] = 1

    def viewable(row, col):
        # look left & right
        # and look up and down (except for the current tree)

        if (
            np.sum(data[row, :col] >= data[row,col]) >= 1
            and np.sum(data[row, col+1:] >= data[row,col]) >= 1
            and np.sum(data[:row, col] >= data[row,col]) >= 1
            and np.sum(data[row+1:, col] >= data[row,col]) >= 1
        ):
            # the tree can not be seen
            visible[row, col] = 0
        else:
            # tree can be seen
            visible[row, col] = 1

    # Loop over the array
    for row in range(rows):
        for col in range(cols):
            viewable(row, col)

    # Print the number of visible trees
    print(np.sum(visible))


    #//FOR PART TWO//


    def scenic_score(row, col):
        # returns the count of visible trees
        # looking right, left, up, down
        score = 1
        curr_tree = data[row, col]
        left = data[row, :col] >= curr_tree
        right = data[row, col + 1:] >= curr_tree
        up = data[:row, col] >= curr_tree
        down = data[row + 1:, col] >= curr_tree
        # left:
        c = 0
        for i in range(len(left) - 1, -1, -1):
            if len(left) < 1:
                break
            c += 1
            if left[i] == True:
                break
        score *= c
        # up:
        c = 0
        for i in range(len(up) - 1, -1, -1):
            if len(up) < 1:
                break
            c += 1
            if up[i] == True:
                break
        score *= c
        # right:
        c = 0
        for i in range(len(right)):
            if len(right) < 1:
                break
            c += 1
            if right[i] == True:
                break
        score *= c
        # down:
        c = 0
        for i in range(len(down)):
            if len(down) < 1:
                break
            c += 1
            if down[i] == True:
                break
        score *= c
        return score

    #array to store the scores
    scores = np.zeros((rows, cols), dtype=int)

    #loop over the array
    for row in range(rows):
        for col in range(cols):
            scores[row, col] = scenic_score(row, col)

    #for debugging
    print(scores)
    #print the max score
    print(np.max(scores))



if __name__ == "__main__":
    main()