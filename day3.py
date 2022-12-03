import string

nums = list(range(1,53))
letters = {string.ascii_letters[i]: nums[i] for i in range(52)}
priority_sum = 0

with open('inputs/day3data.txt', 'r') as file:
    for line in file:
        num_split_items = int(len(line.replace('\n', '')) / 2)
        first = line[:num_split_items]
        second = line[num_split_items:]
        match = []
        for letter in second:
            if letter in first:
                match.append(letter)
            else:
                pass
        for j in set(match):
            priority_sum += letters[j]
print(priority_sum)

# part 2
priority_sum = 0
with open('inputs/day3data.txt', 'r') as file:
    sacks = []
    for line in file:
        sacks.append(line.replace('\n', ''))
        if len(sacks) == 3:
            common = set.intersection(*map(set, sacks))
            for letter in common:
                priority_sum += letters[letter]
            sacks = []
        else:
            pass
print(priority_sum)