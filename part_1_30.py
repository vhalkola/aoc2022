
# Open the input file
fo = open('input.txt', 'r')

# Initialize count of overlapping assignments
overlapping = 0

# Iterate over each entry in the input
for entry in fo:
  # Split each entry into two ranges
  range1 = entry.split(',')[0] 
  range2 = entry.split(',')[1] 
  
  # Extract the beginning and ending of each range
  start1, end1 = map(int, range1.split('-')) 
  start2, end2 = map(int, range2.split('-')) 

  # Compare if one range contains the other
  if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1): 
    overlapping += 1

print ("Number of assignment pairs where one range contains the other: " + str(overlapping))

fo.close()
