def min_max(depth, node_index, is_max, scores):
    if depth == 3:
        return scores[node_index]
    
    if is_max:
        return max(min_max(depth+1, node_index*2, False, scores),
                   min_max(depth+1, node_index*2 + 1, False, scores))
    else:
        return min(min_max(depth+1, node_index*2, True, scores),
                   min_max(depth+1, node_index*2 + 1, True, scores))

scores = [3, 5, 6, 9, 1, 2, 0, -1]
result = min_max(0, 0, True, scores)
print("Min-Max result:", result)
