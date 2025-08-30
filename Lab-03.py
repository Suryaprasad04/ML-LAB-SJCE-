import numpy as np
import matplotlib.pyplot as plt

X=np.random.randn(100)
Y=np.random.randn(100)

X, Y = np.meshgrid(X, Y)

Z=np.sin(X**2+Y**2)

contour = plt.contourf(X, Y, Z, cmap='coolwarm')
plt.colorbar(contour)
plt.title('Filled Contour Plot')
plt.show()

# A contour plot is a 2D way of showing a 3D surface.

# Instead of drawing the whole 3D surface, it uses curved lines (contours) to connect points that have the same value of Z (like height).

# 👉 Think of a geographical map:

# Lines on a map that show the same elevation (like 100m, 200m, 300m) → those are contour lines.

# Closer lines = steeper slope, farther lines = gentle slope.


from queue import PriorityQueue
def a_star(graph,h,start,goal):
    open_set=PriorityQueue()
    open_set.put((0, start))
    came_from={}
    g_score={node:float('inf') for node in graph}
    g_score[start]=0

    while not open_set.empty():
        _, current = open_set.get()

        
        if current == goal:
            print("Reached:", current)   # ✅ just prints the goal
            return current      # reverse to get correct order
        


        for neighbor, cost in graph[current]:
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h[neighbor]
                open_set.put((f_score, neighbor))
    return None  # No path found




# Simple graph
graph = {
    'A': [('B', 1)],
    'B': [('C', 1)],
    'C': []
}

# Heuristic values (distance guess to goal 'C')
h = {
    'A': 2,
    'B': 1,
    'C': 0
}

a_star(graph, h, 'A', 'C')





# Algorithm Steps

# Put the start node in the open set with priority f = g + h.

# While open set is not empty:

# Pick the node with the smallest f.

# If this node is the goal, stop (path found).

# Otherwise, for each neighbor:

# Calculate new cost (tentative_g = g(current) + edge_cost).

# If this path is better, update:

# came_from (to reconstruct path later).

# g_score[neighbor].

# f_score = g + h.

# Add neighbor to open set.

# Repeat until goal is reached or no nodes l
