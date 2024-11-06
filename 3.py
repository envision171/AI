import math


# Define Alpha-Beta Pruning function
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    # Base case: leaf node
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Loop over child nodes
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Loop over child nodes
            eval = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval


# Sample tree values at leaf nodes (3 levels deep, 8 leaf nodes)
values = [3, 65, 6, 9, 1, 2, 0, -1]

# Execute Alpha-Beta Pruning
best_score = alpha_beta_pruning(0, 0, True, values, -math.inf, math.inf)
print("The optimal value is:", best_score)
