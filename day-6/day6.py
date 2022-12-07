# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of four characters that are all different.

# The device will send your subroutine a datastream buffer(your puzzle input)
# your subroutine needs to identify the first position where the four most recently received characters were all different. Specifically, it needs to report the number of characters from the beginning of the buffer to the end of the first such four-character marker.

# For example, suppose you receive the following datastream buffer:

# mjqjpqmgbljsphdztnvjfqwrcgsmlb
# After the first three characters(mjq) have been received, there haven't been enough characters received yet to find the marker. The first time a marker could occur is after the fourth character is received, making the most recent four characters mjqj. Because j is repeated, this isn't a marker.

# The first time a marker appears is after the seventh character arrives. Once it does, the last four characters received are jpqm, which are all different. In this case, your subroutine should report the value 7, because the first start-of-packet marker is complete after 7 characters have been processed.

# Here are a few more examples:

# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11
# How many characters need to be processed before the first start-of-packet marker is detected?

import sys

def main():
    # open the file
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # get the data
    data = lines[0].strip()

    # find the first marker
    marker = find_marker(data)

    # print the result
    print(marker)
    
    #//FOR PART TWO//#
    markerpt2 = find_marker_pt2(data)
    print(markerpt2)

def find_marker(data):
    # initialize the marker
    marker = ''

    # loop through the data
    for i in range(len(data)):
        # add the next character to the marker
        marker += data[i]

        # if the marker is 4 characters long
        if len(marker) == 4:
            # if the marker is unique
            if len(set(marker)) == 4:
                # return the index
                return i + 1

            # remove the first character from the marker
            marker = marker[1:]

    # return -1 if no marker is found
    return -1

def find_marker_pt2(data):
#    A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.


# Here are the first positions of start-of-message markers for all of the above examples:

# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
# How many characters need to be processed before the first start-of-message marker is detected?

    # initialize the marker
    marker = ''

    # loop through the data
    for i in range(len(data)):
        # add the next character to the marker
        marker += data[i]

        # if the marker is 14 characters long
        if len(marker) == 14:
            # if the marker is unique
            if len(set(marker)) == 14:
                # return the index
                return i + 1

            # remove the first character from the marker
            marker = marker[1:]

    # return -1 if no marker is found
    return -1

    

if __name__ == '__main__':
    main()
