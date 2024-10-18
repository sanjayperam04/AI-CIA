import math

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, level=0):
    if depth == 0:
        print(f"{'  ' * level}Returning leaf value: {values[nodeIndex]} at depth {depth}, nodeIndex {nodeIndex}")
        return values[nodeIndex]

    if maximizingPlayer:
        bestValue = -math.inf
        print(f"\n{'  ' * level}Maximizing: Depth {depth}, Node Index {nodeIndex}, Initial Best Value: {bestValue}")

        for i in range(2):
            value = minimax(depth - 1, nodeIndex * 2 + i, False, values, alpha, beta, level + 1)
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)
            print(f"{'  ' * level}Maximizing: Updated Best Value: {bestValue} after considering child {nodeIndex * 2 + i}")

            if beta <= alpha:
                print(f"{'  ' * level}Maximizing: Pruning branch at Node Index {nodeIndex} with Alpha: {alpha} and Beta: {beta}")
                break
        return bestValue
    else:
        bestValue = math.inf
        print(f"\n{'  ' * level}Minimizing: Depth {depth}, Node Index {nodeIndex}, Initial Best Value: {bestValue}")

        for i in range(2):
            value = minimax(depth - 1, nodeIndex * 2 + i, True, values, alpha, beta, level + 1)
            bestValue = min(bestValue, value)
            beta = min(beta, bestValue)
            print(f"{'  ' * level}Minimizing: Updated Best Value: {bestValue} after considering child {nodeIndex * 2 + i}")

            if beta <= alpha:
                print(f"{'  ' * level}Minimizing: Pruning branch at Node Index {nodeIndex} with Alpha: {alpha} and Beta: {beta}")
                break
        return bestValue

# Example usage
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    depth = 3
    result = minimax(depth, 0, True, values, -math.inf, math.inf)
    print("\nThe optimal value is:", result)
