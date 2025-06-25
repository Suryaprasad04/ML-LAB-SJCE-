from queue import PriorityQueue

def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        cost, node = pq.get()
        if node == goal:
            print("Reached:", node)
            return
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                pq.put((0, neighbor))

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
best_first_search(graph, 'A', 'D')
