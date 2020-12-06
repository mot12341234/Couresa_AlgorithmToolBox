# Uses python3
import sys

def get_optimal_value(capacity, weights, values, n):
    total_value = 0.

    items = []

    for i in range(n):
        items.append((values[i], weights[i]))

    # sort the item based on its value per weight
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    for (value, weight) in items:
        if capacity == 0:
            return total_value

        loot_weight = min(capacity, weight)
        total_value += loot_weight * value / weight
        capacity -= loot_weight

    return total_value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values, n)
    print("{:.10f}".format(opt_value))
