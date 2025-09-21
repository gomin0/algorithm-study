import sys
from collections import deque
sys.setrecursionlimit(10000)

# 격자 크기 n, m
# 출발 위치 x, y
# 탈출 지점 r, c
# 이동 거리 k
def solution(n, m, x, y, r, c, k):
    directions = ['d', 'l', 'r', 'u']
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    
    dist: int = abs(x-r) + abs(y-c)
    if dist > k or (k-dist) % 2 != 0:
        return "impossible"
    
    answer = None
    found = False
    def dfs(cx, cy, path, steps):
        nonlocal answer, found
        if found:
            return
        if steps == k:
            if cx == r and cy == c:
                answer = path
                found = True
            return
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 1 <= nx <= n and 1 <= ny <= m:
                remain = abs(nx - r) + abs(ny - c)
                if remain > k - steps - 1:
                    continue
                if (k - steps - 1 - remain) % 2 != 0:
                    continue
                dfs(nx, ny, path + directions[i], steps + 1)
    
    dfs(x, y, "", 0)
    
    return answer if answer else "impossible"