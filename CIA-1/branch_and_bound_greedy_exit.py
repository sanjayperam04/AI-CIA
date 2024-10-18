import heapq

def branch_and_bound_greedy_exit(graph, start, goal, heuristic, exit_condition):
    frontier = [(0, start, [])]
    visited = set()
    while frontier:
        (cost_so_far, current, path) = heapq.heappop(frontier)
        if exit_condition(cost_so_far):
            break
        if current in visited:
            continue
        path = path + [current]
        if current == goal:
            return path, cost_so_far
        visited.add(current)
        for next, weight in graph[current]:
            heapq.heappush(frontier, (heuristic(next), next, path))
    return None

# New example: Early termination if cost exceeds 5
def heuristic(x):
    return 1

def exit_condition(cost):
    return cost > 5

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}
print(f"Branch and Bound Greedy Exit result: {branch_and_bound_greedy_exit(graph, 'A', 'D', heuristic, exit_condition)}")
