
# Solution to Part Two

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Find the item type for each group's badges
sum_priorities = 0 
group_size = 3 # Define group size as 3
for i in range(0, len(lines), group_size):
    # Get the rucksacks for the group
    group_rucksacks = lines[i:i+group_size]
    
    # Count the number of each item type in the group
    item_type_counts = {}
    for rucksack in group_rucksacks:
        already_counted = []
        for item_type in rucksack:
            if item_type not in item_type_counts:
                item_type_counts[item_type] = 0
                already_counted.append(item_type)
                item_type_counts[item_type] += 1
            if item_type not in already_counted:
                item_type_counts[item_type] +=1
                already_counted.append(item_type)
         
    # The badge item type is the one that appears in all three rucksacks    
    badge_item_type = None
    for item_type, count in item_type_counts.items():
        if count == group_size:
            badge_item_type = item_type
            break
    assert badge_item_type is not None
    
    # Calculate the priority of the badge item type
    priority = 0
    if badge_item_type.isupper():
        priority = ord(badge_item_type) - 64 + 26
    else:
        priority = ord(badge_item_type) - 96
    sum_priorities += priority

# Print the sum of the priorities
print("The sum of the priorities of the badges is:", sum_priorities)
