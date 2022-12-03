# part 1
with open('inputs/day1data.txt', 'r') as file:
    total_list = []
    temp_list = []
    for line in file:
        if line != '\n':
            num = int(line)
            temp_list.append(num)
        else:
            total_list.append(sum(temp_list))
            temp_list = []
print(max(total_list))
# part 2
sorted_totals = sorted(total_list)
print(sum(sorted_totals[-3:]))