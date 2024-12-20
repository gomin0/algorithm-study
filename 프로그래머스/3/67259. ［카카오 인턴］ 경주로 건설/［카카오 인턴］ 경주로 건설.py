import heapq

def solution(board):
    answer = 0
    
    n = len(board)
    
    prices = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = []
    
    for i in range(4):
        prices[0][0][i] = 0
        heapq.heappush(queue, (0, 0, 0, i)) # 가격, x, y, 방향
    
    while queue:
        price, x, y, d = heapq.heappop(queue)
        
        if x == n-1 and y == n-1:
            return price
        
        for i in range(4):
            dx, dy = direction[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                next_price = price + 100
                if d != i:
                    next_price += 500
                if next_price < prices[nx][ny][i]:
                    prices[nx][ny][i] = next_price
                    heapq.heappush(queue, (next_price, nx, ny, i))
    
    return min(costs[n-1][n-1])