import heapq

def branch_and_bound_greedy(graph, start, goal, heuristic):
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
            heapq.heappush(frontier, (heuristic(next), next, path))
    return None

# New example: Greedy search in a weighted graph with heuristic
def heuristic(x):
    return 1  # Basic heuristic

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
print(f"Branch and Bound Greedy result: {branch_and_bound_greedy(graph, 'A', 'D', heuristic)}")
