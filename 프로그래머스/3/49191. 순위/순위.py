def solution(n, results):
    answer = 0
    
    player = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        player[i][i] = True
    
    for a, b in results:
        player[a-1][b-1] = True
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if player[i][k] and player[k][j]:
                    player[i][j] = True
    
    for i in range(n):
        count = 0
        for j in range(n):
            if player[i][j] or player[j][i]:
                count += 1
        if count == n:
            answer += 1
    
    return answer