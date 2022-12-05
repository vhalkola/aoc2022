
# Read the input file
with open('input.txt', 'r') as f:
    contents = f.read().split('\n')

# Remove any blank lines
contents = [x for x in contents if x]

# Find the items which appear in both compartments in each rucksack
priority_sum = 0
for line in contents:
    comp_1 = line[:len(line)//2]
    comp_2 = line[len(line)//2:]
    for item in set(comp_1):
        if item in comp_2:
            priority_sum += (ord(item) - ord('a') + 1) if item.islower() else (ord(item) - ord('A') + 27)

# Print final answer
print('The sum of the priorities of item types that appear in both compartments of each rucksack is %d.' % priority_sum)
