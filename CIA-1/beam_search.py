def beam_search(problem, beam_width, neighbors, is_goal, score):
    current = [problem]
    while not any(is_goal(node) for node in current):
        next_generation = []
        for node in current:
            next_generation.extend(neighbors(node))
        current = sorted(next_generation, key=score, reverse=True)[:beam_width]
    return [node for node in current if is_goal(node)]

# New example: Find the maximum in a range using a beam of 2
def score(x):
    return -abs(x - 100)

def neighbors(x):
    return [x - 2, x + 2]

def is_goal(x):
    return x == 100

print(f"Beam Search result: {beam_search(30, 2, neighbors, is_goal, score)}")
