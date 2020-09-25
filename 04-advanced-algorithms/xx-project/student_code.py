from queue import (PriorityQueue, )
import math


def get_path(old, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = old[current]
        path.append(current)
    path.reverse()
    return path


def shortest_path(M, start, goal):
    print("shortest path called")
    path_queue = PriorityQueue()
    path_queue.put(start, 0)

    prev = {start: None}
    scores = {start: 0}

    while not path_queue.empty():

        current = path_queue.get()
        if current == goal:
            get_path(prev, start, goal)

        for node in M.roads[current]:
            x = M.intersections[current]
            y = M.intersections[node]
            this_score = scores[current] + math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)
            path_queue.put(node, this_score)
            prev[node] = current

    return get_path(prev, start, goal)
