import heapq

def solution(board):
    answer = 0
    dx: list[int] = [-1, 1, 0, 0]
    dy: list[int] = [0, 0, -1, 1]
    INF: float = float('inf')
    n: int = len(board)
    costs = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    pq = []
    
    for i in range(4):
        costs[0][0][i] = 0
        heapq.heappush(pq, (0, 0, 0, i))  # 가격, x, y, 방향
    
    while pq:
        cost, x, y, direction = heapq.heappop(pq)
        
        if x == n-1 and y == n-1:
            return cost
        
        for i in range(4):
            nx: int = x + dx[i]
            ny: int = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                next_cost: int = cost + 100
                if direction != i:
                    next_cost += 500
                if next_cost < costs[nx][ny][i]:
                    costs[nx][ny][i] = next_cost
                    heapq.heappush(pq, (next_cost, nx, ny, i))