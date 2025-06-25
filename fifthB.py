def alpha_beta(depth, node_index, is_max, scores, alpha, beta):
    if depth == 3:
        return scores[node_index]
    
    if is_max:
        max_eval = float('-inf')
        for i in range(2):
            val = alpha_beta(depth+1, node_index*2 + i, False, scores, alpha, beta)
            max_eval = max(max_eval, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):
            val = alpha_beta(depth+1, node_index*2 + i, True, scores, alpha, beta)
            min_eval = min(min_eval, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_eval

result = alpha_beta(0, 0, True, scores, float('-inf'), float('inf'))
print("Alpha-Beta result:", result)
