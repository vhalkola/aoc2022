
# read input from file
with open("input.txt") as f:
    lines = f.readlines()

# initialize scores
round_score = []
total_score = 0

# loop through the rows of the strategy guide
for line in lines:
    op, goal = line.strip().split()
    player_choice = {
        ('A','X') : 'S',
        ('A','Y') : 'R',
        ('A','Z') : 'P',
        ('B','X') : 'R',
        ('B','Y') : 'P',
        ('B','Z') : 'S',
        ('C','X') : 'P',
        ('C','Y') : 'S',
        ('C','Z') : 'R'
    }[(op,goal)]
    
    # calculate the winner for the round
    winner = "T"
    if ((op == 'A' and player_choice == 'P') or (op == 'C' and player_choice == 'R') or (op == 'B' and player_choice == 'S')):
        winner = "P"
    elif ((op == 'A' and player_choice == 'S') or (op == 'C' and player_choice == 'P') or (op == 'B' and player_choice == 'R')):
        winner = "O"
    
    # score based on result
    round_score_calc = 0
    if winner == 'P':
        round_score_calc = 6
    elif winner == 'O':
        round_score_calc = 0
    else:
        round_score_calc = 3

    # adding current round score to total
    if player_choice == 'R':
        round_score_calc += 1
    elif player_choice == 'P':
        round_score_calc += 2
    elif player_choice == 'S':
        round_score_calc += 3
    round_score.append(round_score_calc)
    total_score += round_score_calc

# print answer
print("Part Two Answer: {0} (Round Scores: {1})".format(total_score, round_score))
