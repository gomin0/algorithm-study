from collections import deque

def solution(n, m, x, y, r, c, k):
    # 방향 정의 및 사전순 탐색 보장
    direct = {(1, 0): 'd', (0, -1): 'l', (0, 1): 'r', (-1, 0): 'u'}

    # 목표까지의 맨해튼 거리 계산
    def calculate_distance(x1, y1):
        return abs(x1 - (r - 1)) + abs(y1 - (c - 1))

    # 목표까지 도달 가능한지 사전 검사
    initial_distance = calculate_distance(x - 1, y - 1)
    if initial_distance > k or (k - initial_distance) % 2 != 0:
        return "impossible"

    # BFS 탐색 시작
    queue = deque([(x - 1, y - 1, 0, "")])  # (현재 x, 현재 y, 이동 횟수, 경로)

    while queue:
        si, sj, cnt, route = queue.popleft()

        # 목표 지점 도달 확인
        if (si, sj) == (r - 1, c - 1):
            if cnt == k:
                return route
            if (k - cnt) % 2:  # 남은 거리가 홀수면 도달 불가능
                return "impossible"

        # 사전순으로 네 방향 탐색
        for di, dj in direct:
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < m:
                # 목표까지 도달 가능한지 확인 후 큐에 추가
                next_distance = calculate_distance(ni, nj)
                if next_distance + cnt + 1 <= k:
                    queue.append((ni, nj, cnt + 1, route + direct[(di, dj)]))
                    break  # 한 방향만 추가 (큐 크기 제한)

    return "impossible"