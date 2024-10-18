def hill_climbing(problem, neighbors, is_goal, score):
    current = problem
    while not is_goal(current):
        next = max(neighbors(current), key=score)
        if score(next) <= score(current):
            return current
        current = next
    return current

# New example: Maximize a function f(x) = -abs(x - 50)
def score(x):
    return -abs(x - 50)

def neighbors(x):
    return [x - 1, x + 1]

def is_goal(x):
    return x == 50

print(f"Hill Climbing result: {hill_climbing(30, neighbors, is_goal, score)}")
