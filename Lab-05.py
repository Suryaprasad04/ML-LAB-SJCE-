import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X=[12, 7, 3, 7, 8, 3, 4, 6, 8, 9, 10, 12, 15, 18, 20]
sns.boxplot(x=X)
plt.show()


def alpha_beta(depth,node_index,is_max,scores,alpha,beta):
    if depth==3:
        return scores[node_index]
    
    if is_max:
        max_eval=float('-inf')
        for i in range(0,2):
            val=alpha_beta(depth+1,node_index*2+i,False,scores,alpha,beta)
            max_eval=max(max_eval,val)
            alpha=max(alpha,max_eval)
            if beta<=alpha:
                break
        return max_eval 
    else:
        min_eval=float('inf')
        for i in range(0,2):
            val=alpha_beta(depth+1,node_index*2+i,True,scores,alpha,beta)
            min_eval=min(min_eval,val)
            beta=min(beta,min_eval)
            if beta<=alpha:
                break
        return min_eval 

scores=[9,8,7,6,5,4,3,2]
print(alpha_beta(0,0,True,scores,float('-inf'),float('inf')))





# 🔹 Algorithm in Simple Words

# Max node tries to maximize value.

# Min node tries to minimize value.

# Alpha = best option Max has found so far.

# Beta = best option Min has found so far.

# If ever alpha ≥ beta, stop searching that branch (pruned).




                  (Root, MAX)
                 /            \
        (MIN)                      (MIN)
       /     \                   /       \
   (MAX)     (MAX)           (MAX)       (MAX)
   /  \       /  \           /   \        /   \
 9    8     7    6        5      4      3     2
🔹 How Alpha-Beta Pruning Helps

Normally, minimax would check all 8 leaves.
But alpha-beta pruning cuts off branches when they can’t affect the final decision.

Example of pruning in this tree:

Left subtree evaluated first → result = 7

Alpha updated = 7

While evaluating right subtree:

First branch (5,4) gives 5

Now MIN node has 5, Beta = 5

Compare with Alpha (7). Since beta ≤ alpha (5 ≤ 7) → stop exploring more

So the (3,2) branch is pruned (not evaluated at all).
