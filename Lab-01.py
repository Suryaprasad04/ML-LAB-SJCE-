import numpy as np
import matplotlib.pyplot as plt

X=[1,2,3,4,5]
Y=[2,3,5,7,11]

plt.scatter(X,Y)
plt.title("Scatter Plot Example")
plt.show()



def hill_climbing():
    def fitness(x):
        return -1*(x-3)**2+9
    current=0
    step=0.1

    while True:
        next=current+step
        if fitness(next)>fitness(current):
            current=next
        else:
            break
    print("Optimal solution:",current)
    print("Optimal value:",fitness(current))

hill_climbing()





# 🌄 Hill Climbing Algorithm (Concept)

# A simple optimization algorithm.

# Steps:

# Start with a random/initial solution.

# Look at "neighbor" solutions (small changes).

# Move to the neighbor if it improves the result.

# Repeat until no better solution is found (local maximum/minimum).

# 👉 In your case:

# Searching along a curve f(x) = - (x-3)² + 9.

# Algorithm starts at x=0, keeps moving right, stops when it reaches the peak near x=3.
