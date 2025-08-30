import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data=np.random.rand(10, 12)
sns.heatmap(data)
plt.show()

def min_max(depth,node_index,is_max,scores):
    if depth==3:
        return scores[node_index]
    
    if is_max:
        return max(min_max(depth+1,node_index*2,False,scores),
                   min_max(depth+1,node_index*2+1,False,scores))
    else:
        return min(min_max(depth+1,node_index*2,True,scores),
                   min_max(depth+1,node_index*2+1,True,scores))

scores=[9, 8, 7, 6, 5, 4, 3, 2]
print(min_max(0,0,True,scores))



# 🔹 Min-Max Algorithm (Explanation)

# What it is

# Min-Max is a decision-making algorithm used in games (like Tic-Tac-Toe, Chess).

# Two players:

# Maximizer → tries to get the highest score.

# Minimizer → tries to get the lowest score.

# They take turns choosing moves.

# The algorithm explores all possible moves (game tree) and decides the best one for the Maximizer.


                         (Root, depth=0, MAX)
                       /                      \
          (depth=1, MIN)                       (depth=1, MIN)
          /          \                         /            \
 (depth=2, MAX)   (depth=2, MAX)       (depth=2, MAX)   (depth=2, MAX)
   / \                / \                / \                / \
 [9] [8]           [7] [6]            [5] [4]           [3] [2]
