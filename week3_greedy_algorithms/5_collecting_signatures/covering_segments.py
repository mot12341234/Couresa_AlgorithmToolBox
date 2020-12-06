# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # for s in segments:
    #     points.append(s.start)
    #     points.append(s.end)
    # return points

    # rank the segment based on its end point
    segments.sort(key=lambda x: x.end)

    current = segments[0].end
    points.append(current)
    for segment in segments:
        if current < segment.start:
            current = segment.end
            points.append(current)

    return points


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *data = map(int, input().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
