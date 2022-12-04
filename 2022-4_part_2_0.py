
# Initialize overlapping assignmnet pairs counter to 0
overlapping_pairs = 0

# Read in input from file
with open('input.txt', 'r') as input_file:
    pairs = [pair.strip('\n').split(',') for pair in input_file.readlines()]

# Loop through all pair assignments
for i in range(len(pairs)):
    assignment_pair_1, assignment_pair_2 = pairs[i]

    # Split each assignment into individual sections
    sections_pair_1 = [int(x) for x in assignment_pair_1.split('-')]
    sections_pair_2 = [int(x) for x in assignment_pair_2.split('-')]

    # Calculate first range boundaries
    start_1 = min(sections_pair_1)
    end_1 = max(sections_pair_1)

    # Calculate second range boundaries
    start_2 = min(sections_pair_2)
    end_2 = max(sections_pair_2)

    # Compare range 1 with range 2
    if start_2 <= end_1 and end_2 >= start_1:
        overlapping_pairs += 1

    # Compare range 2 with range 1
    elif start_1 <= end_2 and end_1 >= start_2:
        overlapping_pairs += 1

# Print answer
print("The number of overlapping assignment pairs is %d" % overlapping_pairs)
