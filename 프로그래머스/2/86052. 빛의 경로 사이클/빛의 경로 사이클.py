def solution(grid):  # gird = ["SL","LR"]
    answer = []
    dy = (1, 0, -1, 0)
    dx = (0, 1, 0, -1)
    
    n = len(grid)
    m = len(grid[0])
    
    # 4방향 방문 체크 -> 같은 방향으로 또 방문한다 => 순환
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for d in range(4):
                if visited[i][j][d]:
                    continue
                count = 0
                ny, nx = i, j
                while not visited[ny][nx][d]:
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == 'R':
                        d = (d-1) % 4
                    elif grid[ny][nx] == 'L':
                        d = (d+1) % 4
                    ny = (ny + dy[d]) % n
                    nx = (nx + dx[d]) % m
                answer.append(count)
    return sorted(answer)