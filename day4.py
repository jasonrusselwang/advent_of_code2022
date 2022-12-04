with open('inputs/day4data.txt', 'r') as file:
    counter = 0
    for line in file:
        # convert to range
        range1, range2 = line.replace('\n', '').split(',')
        range1a, range1b = range1.split('-')
        range2a, range2b = range2.split('-')
        range1 = range(int(range1a), int(range1b) + 1)
        range2 = range(int(range2a), int(range2b) + 1)
        # check if one fully overlaps another by checking if the first and last values of one range fall into the other range
        if (range1[0] in range2 and range1[-1] in range2) or (range2[0] in range1 and range2[-1] in range1):
            counter += 1
    print(counter)

# part 2
with open('inputs/day4data.txt', 'r') as file:
    counter = 0
    for line in file:
        range1, range2 = line.replace('\n', '').split(',')
        range1a, range1b = range1.split('-')
        range2a, range2b = range2.split('-')
        # if the total range of the two lists has n numbers, then the sum of the values in both ranges will be greater ONLY when there is overlapping values
        if max(int(range1b) + 1, int(range2b) + 1) - min(int(range1a), int(range2a)) < (int(range1b) + 1 - int(range1a)) + (int(range2b) + 1 - int(range2a)):
            counter += 1
    print(counter)