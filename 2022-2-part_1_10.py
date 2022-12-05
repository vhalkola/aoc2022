
# Open file
with open('input.txt', 'r') as f:
    # Read the lines
    lines = f.readlines()

# Predefined scores for winning, losing, and drawing
score = {'win': 6, 'lose': 0, 'draw': 3}

# Initialize the total score to 0
total_score = 0

# Loop over each line
for line in lines:
    # Remove the newline character
    line = line.strip()
    
    # Record the opponent's move
    opponent_move = line[0]
    
    # Record the move in the strategy
    strategy_move = line[2]
    
    # Compare opponent and strategy move
    if (opponent_move == 'A' and strategy_move == 'X') or (opponent_move == 'B' and strategy_move == 'Y') or (opponent_move == 'C' and strategy_move == 'Z'):
        # Draw
        outcome = 'draw'
    elif (opponent_move == 'A' and strategy_move == 'Y') or \
         (opponent_move == 'B' and strategy_move == 'Z') or \
         (opponent_move == 'C' and strategy_move == 'X'):
        # Win
        outcome = 'win'
    else:
        # Lose
        outcome = 'lose'
    
    # Calculate the score for the round
    round_score = 1 if strategy_move == 'X' else 2 if strategy_move == 'Y' else 3
    round_score += score[outcome]
    
    # Add to total score
    total_score += round_score

# Print total score
print(f'Total score: {total_score}')
