class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []

def alpha_beta_pruning(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = float('-inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in node.children:
            eval = alpha_beta_pruning(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def build_game_tree():
    root = Node()
    level1 = [Node() for _ in range(2)]
    root.children = level1
    level2 = [Node(value=-1 if i % 2 == 0 else 1) for i in range(4)]
    for i in range(2):
        level1[i].children = level2[i * 2:(i + 1) * 2]
    return root

def simulate_game(first_player):
    current_player = first_player  # 0 for Scorpion, 1 for Sub-Zero
    total_rounds = 3  # You can adjust this value for more rounds
    round_winners = []
    for round_num in range(1, total_rounds + 1):
        game_tree = build_game_tree()
        winner_value = alpha_beta_pruning(game_tree, 5, float('-inf'), float('inf'), current_player == 0)
        round_winner = "Scorpion" if winner_value == -1 else "Sub-Zero"
        round_winners.append(f"Winner of Round {round_num}: {round_winner}")
        current_player = 1 - current_player  # Alternate starting player

    # Determine the overall winner (most rounds won)
    scorpion_wins = sum(1 for winner in round_winners if "Scorpion" in winner)
    sub_zero_wins = total_rounds - scorpion_wins
    game_winner = "Scorpion" if scorpion_wins > sub_zero_wins else "Sub-Zero"

    # Print results
    print(f"Game Winner: {game_winner}")
    print(f"Total Rounds Played: {total_rounds}")
    for result in round_winners:
        print(result)

# Example Input: 0 (Scorpion starts first)
simulate_game(0)
