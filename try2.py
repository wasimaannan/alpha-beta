def pacman_game(c):
    leaf_nodes = [3, 6, 2, 3, 7, 1, 2, 0]

    def minimax(depth, node_index, maximizing_player):
        if depth == 3:
            return leaf_nodes[node_index]

        if maximizing_player:
            return max(
                minimax(depth + 1, node_index * 2, False),
                minimax(depth + 1, node_index * 2 + 1, False)
            )
        else:
            return min(
                minimax(depth + 1, node_index * 2, True),
                minimax(depth + 1, node_index * 2 + 1, True)
            )

    no_dark_magic = minimax(0, 0, True)

    # Calculate the effect of using dark magic
    dark_magic_left = max(leaf_nodes[:4]) - c
    dark_magic_right = max(leaf_nodes[4:]) - c

    if dark_magic_left > no_dark_magic or dark_magic_right > no_dark_magic:
        best_move = "right" if dark_magic_right > dark_magic_left else "left"
        dark_magic_value = max(dark_magic_left, dark_magic_right)
        print(f"With dark magic, Pacman goes {best_move} and achieves score {dark_magic_value}.")
    else:
        print(f"Without dark magic, Pacman achieves score {no_dark_magic}.")

pacman_game(2)  # Example input
