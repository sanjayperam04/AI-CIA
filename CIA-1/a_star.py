import heapq

def a_star(graph, start, goal, heuristic):
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
            heapq.heappush(frontier, (cost_so_far + weight + heuristic(next), next, path))
    return None

# New example: A* search in a weighted graph
def heuristic(x):
    return 1

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
print(f"A* Algorithm result: {a_star(graph, 'A', 'D', heuristic)}")
