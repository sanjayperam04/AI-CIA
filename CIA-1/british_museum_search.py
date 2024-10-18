import random

def british_museum_search(possible_solutions, is_goal):
    # Exhaustively checks all possible solutions
    for solution in possible_solutions:
        if is_goal(solution):
            return solution
    return None

# New logic: Find the square root of 16
def is_goal(solution):
    return solution ** 2 == 16  # Goal: Find number whose square is 16

possible_solutions = random.sample(range(10), 10)
result = british_museum_search(possible_solutions, is_goal)
print(f"Solution found: {result}")
