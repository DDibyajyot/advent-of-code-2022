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


    



if __name__ == "__main__":
    main()