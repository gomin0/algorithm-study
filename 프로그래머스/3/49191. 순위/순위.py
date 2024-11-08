def solution(n, results):
    answer = 0
    
    reachable = [[False] * n for _ in range(n)]  # 이기면 True
    
    for a, b in results:
        reachable[a-1][b-1] = True
    
    # 플로이드 워셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reachable[i][k] and reachable[k][j]:
                    reachable[i][j] = True
    
    for i in range(n):
        count = 0
        for j in range(n):
            if reachable[i][j] or reachable[j][i]:  # 승패 관계 개수
                count += 1
        if count == n - 1:
            answer += 1
    
    return answer