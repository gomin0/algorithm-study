from itertools import combinations
import sys


def select_chicken(chicken, m):
    m_chicken = list(combinations(chicken, m))
    return m_chicken


def get_chicken_distance(house, chicken_comb):
    total_distance = 0
    for hi, hj in house:
        distance = float('inf')
        for ci, cj in chicken_comb:
            distance = min(distance, abs(ci - hi) + abs(cj - hj))
        total_distance += distance
    return total_distance


n, m = map(int, sys.stdin.readline().split())

graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


house = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

m_chicken = select_chicken(chicken, m)
chicken_distance = float('inf')
for chicken_comb in m_chicken:
    city_distance = get_chicken_distance(house, chicken_comb)
    chicken_distance = min(chicken_distance, city_distance)

print(chicken_distance)