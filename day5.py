# load in initial setup
with open('inputs/day5data.txt', 'r') as file:
    moves = False
    stacks = {}
    for line in file:
        if line == '\n': # if newline, then moves are starting
            moves = True
        elif moves:
            # process move
            transfer, source, dest = [int(i) for i in line.split() if i.isdigit()]
            # move transfer items to front of destination
            stacks[dest][0:0] = stacks[source][:transfer][::-1]
            # remove transferred item from source
            stacks[source] = stacks[source][transfer:]
        else: # create stacks; script will start here
            # line string has a space between stacks, need to offset 4 to 3
            # every 3 is a block, empty or not
            blocks = [line.replace('\n', '')[i:i+3] for i in range(0, len(line), 4)]
            for stack in range(len(blocks)):
                if '[' in blocks[stack]:
                    stacks.setdefault(stack + 1, []).append(blocks[stack].replace('[', '').replace(']', ''))
solution = ''.join([stacks[i + 1][0] for i in range(len(stacks.keys()))])
print(f'Part 1 Solution: {solution}')

# part 2
# literally the same solution as part 1 except we dont have to reverse the transfer list
# order is maintained rather than moving one crate at a time on top of the other
with open('inputs/day5data.txt', 'r') as file:
    moves = False
    stacks = {}
    for line in file:
        if line == '\n': # if newline, then moves are starting
            moves = True
        elif moves:
            # process move
            transfer, source, dest = [int(i) for i in line.split() if i.isdigit()]
            # move transfer items to front of destination
            stacks[dest][0:0] = stacks[source][:transfer]
            # remove transferred item from source
            stacks[source] = stacks[source][transfer:]
        else: # create stacks
            # line string has a space between stacks, need to offset 4 to 3
            # every 3 is a block, empty or not
            blocks = [line.replace('\n', '')[i:i+3] for i in range(0, len(line), 4)]
            for stack in range(len(blocks)):
                if '[' in blocks[stack]:
                    stacks.setdefault(stack + 1, []).append(blocks[stack].replace('[', '').replace(']', ''))
solution = ''.join([stacks[i + 1][0] for i in range(len(stacks.keys()))])
print(f'Part 2 Solution: {solution}')