# AI Search Algorithm Implementations

This repository contains implementations of various algorithms commonly used in search and optimization problems. Each algorithm is described below, along with its purpose and key characteristics.

## Table of Contents
1. [British Museum Search](#british-museum-search)
2. [Depth-First Search (DFS)](#depth-first-search-dfs)
3. [Breadth-First Search (BFS)](#breadth-first-search-bfs)
4. [Hill Climbing](#hill-climbing)
5. [Beam Search](#beam-search)
6. [Oracle](#oracle)
7. [Branch and Bound (B&B)](#branch-and-bound-bb)
8. [Branch & Bound Greedy](#branch--bound-greedy)
9. [Branch & Bound Greedy with Exit](#branch--bound-greedy-with-exit)
10. [Branch & Bound Greedy with Heuristic](#branch--bound-greedy-with-heuristic)
11. [Branch & Bound Heuristic](#branch--bound-heuristic)
12. [A* Algorithm](#a-algorithm)

## Algorithms

### British Museum Search
- **Description**: A search algorithm inspired by the British Museum, focusing on optimizing the search for items within a vast dataset.
- **Use Cases**: Suitable for scenarios where structured search within a large dataset is required.

### Depth-First Search (DFS)
- **Description**: A traversal algorithm that explores as far as possible along each branch before backtracking.
- **Complexity**: O(V + E) where V is the number of vertices and E is the number of edges.
- **Use Cases**: Useful for pathfinding, topological sorting, and solving puzzles.

### Breadth-First Search (BFS)
- **Description**: A traversal algorithm that explores all neighbors at the present depth prior to moving on to nodes at the next depth level.
- **Complexity**: O(V + E).
- **Use Cases**: Finding the shortest path in unweighted graphs and level-order traversal of trees.

### Hill Climbing
- **Description**: An optimization algorithm that continuously moves towards increasing value (uphill) until no higher value can be found.
- **Use Cases**: Used in mathematical optimization problems, artificial intelligence, and game development.

### Beam Search
- **Description**: A search algorithm that explores a graph by expanding the most promising nodes, keeping a limited number of paths (the beam width).
- **Use Cases**: Often used in natural language processing and AI.

### Oracle
- **Description**: An algorithm that leverages a "black box" for obtaining solutions, often used in theoretical computer science.
- **Use Cases**: Analyzing decision-making processes and optimizing queries.

### Branch and Bound (B&B)
- **Description**: An optimization technique that divides the problem into smaller subproblems and systematically explores branches to find the optimal solution.
- **Use Cases**: Solving combinatorial optimization problems.

### Branch & Bound Greedy
- **Description**: A variant of the B&B algorithm that employs a greedy approach to make local optimal choices.
- **Use Cases**: Used in optimization problems where a quick, good-enough solution is acceptable.

### Branch & Bound Greedy with Exit
- **Description**: An extension of the greedy approach that allows for early exits from the search if a satisfactory solution is found.
- **Use Cases**: Applicable in real-time systems where time constraints are critical.

### Branch & Bound Greedy with Heuristic
- **Description**: Combines the greedy approach with heuristics to guide the search process.
- **Use Cases**: Useful in scenarios where heuristics can significantly reduce the search space.

### Branch & Bound Heuristic
- **Description**: An approach that uses heuristics to determine the most promising nodes to explore in the B&B algorithm.
- **Use Cases**: Enhancing the efficiency of traditional B&B algorithms in large search spaces.

### A* Algorithm
- **Description**: A pathfinding algorithm that combines the strengths of Dijkstra's Algorithm and heuristics to find the shortest path efficiently.
- **Complexity**: O(E) where E is the number of edges.
- **Use Cases**: Widely used in AI for navigation and pathfinding in games.

## Getting Started

### Prerequisites
- Python 3.x
- Required libraries (if any, specify here)

### Contributing
Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to get started.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
