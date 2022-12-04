import sys

def main():
    # open the file
    with open(sys.argv[1]) as f:
        lines = f.readlines()

   #initialize the number of pairs that contain each other
    pairs_contain_each_other = 0

    #for each line
    for line in lines:
        #get the two ranges
        r1 = line.split(",")[0]
        r2 = line.split(",")[1]

        #get the start and end of each range
        r1_start = int(r1.split("-")[0])
        r1_end = int(r1.split("-")[1])
        r2_start = int(r2.split("-")[0])
        r2_end = int(r2.split("-")[1])

        #if the start of r1 is greater than the start of r2 and the end of r1 is less than the end of r2
        if r1_start >= r2_start and r1_end <= r2_end:
            #increment the number of pairs that contain each other
            pairs_contain_each_other += 1
        #if the start of r2 is greater than the start of r1 and the end of r2 is less than the end of r1
        elif r2_start >= r1_start and r2_end <= r1_end:
            #increment the number of pairs that contain each other
            pairs_contain_each_other += 1

    #print the number of pairs that contain each other
    print(pairs_contain_each_other)

    #//FOR PART TWO//
    #initialize the number of pairs that overlap
    pairs_overlap = 0

    #for each line
    for line in lines:
        #get the two ranges
        r1 = line.split(",")[0]
        r2 = line.split(",")[1]

        #get the start and end of each range
        r1_start = int(r1.split("-")[0])
        r1_end = int(r1.split("-")[1])
        r2_start = int(r2.split("-")[0])
        r2_end = int(r2.split("-")[1])

#use set intersection to solve it
        #get the intersection of the two ranges
        intersection = set(range(r1_start, r1_end + 1)).intersection(set(range(r2_start, r2_end + 1)))

        #if the intersection is not empty
        if intersection:
            #increment the number of pairs that overlap
            pairs_overlap += 1




    #print the number of pairs that overlap
    print(pairs_overlap)

if __name__ == "__main__":
    main()

#well got 2125 for the first star but wasted too much time on the second star doing the exact opposite of what 
# we were supposed to do so I'm just gonna leave it at that