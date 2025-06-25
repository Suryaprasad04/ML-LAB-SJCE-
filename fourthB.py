from queue import PriorityQueue

def a_star(graph, h, start, goal):
    open_set = PriorityQueue()
    open_set.put((h[start], start))
    came_from = {}

    g = {node: float('inf') for node in graph}
    g[start] = 0

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            print("Reached:", current)
            return

        for neighbor, cost in graph[current]:
            tentative_g = g[current] + cost
            if tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f = g[neighbor] + h[neighbor]
                open_set.put((f, neighbor))

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3)],
    'C': [('D', 1)],
    'D': []
}
h = {'A': 4, 'B': 2, 'C': 2, 'D': 0}
a_star(graph, h, 'A', 'D')
