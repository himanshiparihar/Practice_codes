import sys
import unittest


def get_optimal_value1(capacity, weights, values):
    value2 = 0.
    proportion = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            return value2
            break
        max_weight = max(proportion)
        index = proportion.index(max_weight)
        proportion[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
    return value2


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value1(capacity, weights, values)
    print("{:.10f}".format(opt_value))