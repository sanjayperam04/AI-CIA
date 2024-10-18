def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))
    return None

# New example: Search in a maze-like structure
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
print(f"DFS path from A to F: {dfs(graph, 'A', 'F')}")
