from collections import deque

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

# New example: Find the shortest path in a grid
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
print(f"BFS path from A to F: {bfs(graph, 'A', 'F')}")
