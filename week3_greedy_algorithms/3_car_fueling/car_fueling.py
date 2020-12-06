# python3
import sys


def compute_min_refills(distance, tank, stops):

    gas_fill = 0
    # append the destination into the stops
    stops.append(distance)

    # record the last time filling gas
    last_gas_fill = 0
    for i in range(len(stops) - 1):
        if (stops[i] - last_gas_fill) < tank and (stops[i+1] - last_gas_fill) < tank:
            continue
        elif (stops[i] - last_gas_fill) < tank < (stops[i + 1] - last_gas_fill):
            gas_fill += 1
            last_gas_fill = stops[i]
        elif stops[i] - last_gas_fill > tank:
            return - 1

    return gas_fill


if __name__ == '__main__':
    # d, m, _, *stops = map(int, sys.stdin.read().split())
    d, m, _, *stops = map(int, input().split())
    print(compute_min_refills(d, m, stops))
