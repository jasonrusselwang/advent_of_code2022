with open('inputs/day6data.txt', 'r') as file:
    for line in file:
        data = line.replace('\n', '')
        for i in range(3, len(data) + 1):
            # create window to interate over
            subset = data[i-3:i+1]
            # if the unique set is the same length of the subset variable then there are no repeats
            if len(set(subset)) == len(subset):
                break
        print(f'Part 1 Solution: {i + 1}')        

# part 2
# same solution, different sized window
with open('inputs/day6data.txt', 'r') as file:
    for line in file:
        data = line.replace('\n', '')
        for i in range(13, len(data) + 1):
            # create window to interate over
            subset = data[i-13:i+1]
            # if the unique set is the same length of the subset variable then there are no repeats
            if len(set(subset)) == len(subset):
                break
        print(f'Part 2 Solution: {i + 1}')    