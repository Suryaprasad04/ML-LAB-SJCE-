import numpy as np
import matplotlib.pyplot as plt


x = np.random.randn(100)   # 1D data
y = np.random.randn(100)

X, Y = np.meshgrid(x, y)   # make 2D grid
Z = np.sin(np.sqrt(X**2 + Y**2))  # compute Z on grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # 3D plot

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("3D Surface Plot Example")

plt.show()





from queue import PriorityQueue
def bfs(graph,start,goal):
    visited=set()
    pq=PriorityQueue()
    pq.put((0,start))

    while not pq.empty():
        cost,node=pq.get()
        if node==goal:
            print("Reached:", node)
            return  cost
        if node not in visited:
            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    pq.put((cost+1,neighbor))



graph={
    'A':['B','C'],
    'B':['C'],
    'C':['A']  
}
print(bfs(graph,'A','C'))




# Algorithm

# Start with the initial node (start) and insert it into a priority queue with priority = 0.

# Keep a set of visited nodes.

# While the priority queue is not empty:

# Remove the node with the lowest cost from the queue.

# If this node is the goal, return success (and cost).

# If not visited yet:

# Mark it as visited.

# Insert all unvisited neighbors into the priority queue with updated cost (cost + 1).

# Continue until the goal is found or queue becomes empty.
