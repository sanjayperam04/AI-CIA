# Simulating an Oracle search algorithm using predefined oracle hints
def oracle_search(graph, start, goal, oracle):
    path = [start]
    current_node = start
    while current_node != goal:
        next_node = oracle(graph, current_node, goal)  # Ask the oracle for the next step
        if not next_node:
            return None  # No path found
        path.append(next_node)
        current_node = next_node
    return path

# Example Oracle function: Choose the first available neighbor or the goal if nearby
def oracle(graph, current_node, goal):
    if goal in graph[current_node]:
        return goal  # Go directly to the goal if it's a neighbor
    return graph[current_node][0] if graph[current_node] else None  # Otherwise, pick the first neighbor

# Example graph
graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}

# Run Oracle Search
print(f"Oracle Search path from A to F: {oracle_search(graph, 'A', 'F', oracle)}")
