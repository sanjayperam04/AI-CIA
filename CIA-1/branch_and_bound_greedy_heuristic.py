import heapq

def branch_and_bound_greedy_heuristic(graph, start, goal, greedy_heuristic, cost_heuristic):
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
            heapq.heappush(frontier, (cost_so_far + weight + greedy_heuristic(next) + cost_heuristic(next), next, path))
    return None

# New example: Combining heuristics and greedy in a weighted graph
def greedy_heuristic(x):
    return 1

def cost_heuristic(x):
    return 2

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
print(f"Branch and Bound Greedy with Heuristic result: {branch_and_bound_greedy_heuristic(graph, 'A', 'D', greedy_heuristic, cost_heuristic)}")
