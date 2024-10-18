import heapq

def branch_and_bound(graph, start, goal):
    frontier = [(0, start, [])]
    visited = set()
    while frontier:
        (cost_so_far, current, path) = heapq.heappop(frontier)
        if current in visited:
            continue
        path = path + [current]
        if current == goal:
            return path, cost_so_far
        visited.add(current)
        for next, weight in graph[current]:
            heapq.heappush(frontier, (cost_so_far + weight, next, path))
    return None

# New example: Shortest path in a weighted graph
graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
print(f"Branch and Bound result: {branch_and_bound(graph, 'A', 'D')}")
