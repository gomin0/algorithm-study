def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        targetX, targetY = ball
        distance = float('inf')
        
        # 왼쪽 벽
        if not (startY == targetY and startX > targetX):
            dist = (startX + targetX) ** 2 + (startY - targetY) ** 2
            distance = min(distance, dist)
        # 오른쪽 벽
        if not (startY == targetY and startX < targetX):
            dist = (2 * m - startX - targetX) ** 2 + (startY - targetY) ** 2
            distance = min(distance, dist)
        # 위쪽 벽
        if not (startX == targetX and startY < targetY):
            dist = (startX - targetX) ** 2 + (2 * n - startY - targetY) ** 2
            distance = min(distance, dist)
        # 아래쪽 벽
        if not (startX == targetX and startY > targetY):
            dist = (startX - targetX) ** 2 + (startY + targetY) ** 2
            distance = min(distance, dist)
        
        answer.append(distance)
    return answer