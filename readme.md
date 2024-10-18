# Graph Search Algorithms & Game Theory Techniques

## Overview
This repository showcases implementations of various graph search algorithms alongside decision-making methods commonly used in game theory. The objective is to identify optimal paths in a graph, moving from a starting node \( S \) to a goal node \( G \), while also exploring strategies like the Minimax algorithm and Alpha-Beta Pruning.

## Graph Structure
The following graph serves as the foundation for all implemented search algorithms:

```python
graph = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}
```

### Heuristic Values
The heuristic values assigned to the nodes are as follows:

```python
heuristic = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}
```

## Search Algorithms
Each algorithm initiates from node \( S \) and aims to reach node \( G \), determining the most efficient path based on distinct methodologies.

### Implemented Algorithms
1. **British Museum Search**  
   A comprehensive approach that evaluates all potential paths.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

2. **Depth-First Search (DFS)**  
   This method delves as deeply as possible into each branch before backtracking.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

3. **Breadth-First Search (BFS)**  
   Explores all nodes at the current depth level prior to advancing to the next level.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

4. **Hill Climbing**  
   A greedy technique that consistently expands the node with the lowest heuristic value.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

5. **Beam Search**  
   Maintains a limited number of top nodes at each level to enhance memory efficiency.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

6. **Oracle Search**  
   A theoretical search method that operates with complete knowledge of the shortest path.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

7. **Branch and Bound (B&B)**  
   This technique investigates all possible paths while eliminating those exceeding the best-known cost.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

8. **Branch and Bound Greedy**  
   Utilizes a heuristic to direct the search process while also trimming paths.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

9. **Branch and Bound Greedy with Exit**  
   Terminates immediately upon reaching the goal node.  
   **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

10. **Branch and Bound Greedy + Heuristic**  
    Aggressively combines cost and heuristic for efficient pruning of the search space.  
    **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

11. **Branch and Bound with Heuristic**  
    Merges the B&B methodology with heuristic values, exploring nodes based on both factors.  
    **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

12. **A* Algorithm**  
    An informed search technique that incorporates both path costs and heuristics to identify the optimal route.  
    **Output:** `Best Path: ['S', 'A', 'D', 'G'] with cost 6`

## Minimax Algorithm & Alpha-Beta Pruning

### Description
The Minimax Algorithm serves as a foundational approach in decision-making for two-player games. The Maximizer focuses on maximizing their score, while the Minimizer aims to minimize it.

**Alpha-Beta Pruning** enhances the Minimax algorithm's efficiency by avoiding the evaluation of branches that will not influence the final decision.

### Mechanism
- **Minimax Algorithm:**
  - Maximizing Player: Attempts to increase the value at each node.
  - Minimizing Player: Seeks to decrease the value at each node.
  - Values are propagated from leaf nodes back to the root.

- **Alpha-Beta Pruning:**
  - Alpha: The maximum score that the Maximizer can assure.
  - Beta: The minimum score that the Minimizer can assure.
  - Branches are pruned when alpha ≥ beta, resulting in greater efficiency.

### Example Tree Structure
Both algorithms utilize the following tree for their evaluations:

```
          N1
        /    \
      N2      N3
     /  \    /  \
   N4   N5  N6   N7
  / \   / \  / \  / \
 1   4 7   2 3   0 6   5
```

### Output
- **Minimax Algorithm:** Optimal value calculated: **5**
- **Alpha-Beta Pruning:** Optimal value achieved: **5**

Both algorithms arrive at the same optimal value, though Alpha-Beta Pruning operates more effectively by eliminating non-critical branches.
