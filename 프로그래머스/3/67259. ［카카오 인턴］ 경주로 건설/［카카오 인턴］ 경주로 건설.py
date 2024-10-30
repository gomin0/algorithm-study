import heapq

def solution(board):
    answer = 0
    
    n = len(board)
    costs = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = []
    
    for i in range(4):
        costs[0][0][i] = 0
        heapq.heappush(queue, (0, 0, 0, i))
    
    while queue:
        current_cost, x, y, direction = heapq.heappop(queue)
        
        if x == n - 1 and y == n - 1:
            return current_cost
        
        for next_direction, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                next_cost = current_cost + 100
                if direction != next_direction:
                    next_cost += 500
                
                if next_cost < costs[nx][ny][next_direction]:
                    costs[nx][ny][next_direction] = next_cost
                    heapq.heappush(queue, (next_cost, nx, ny, next_direction))
    
    return min(costs[n-1][n-1])