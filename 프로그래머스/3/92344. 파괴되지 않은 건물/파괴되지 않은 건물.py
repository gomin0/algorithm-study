def solution(board, skill):
    answer = 0
    
    n, m = len(board), len(board[0])
    skill_sum = [[0] * (m+1) for _ in range(n+1)]
    
    for skill_type, x1, y1, x2, y2, degree in skill:
        if skill_type == 1:
            degree = -degree
        skill_sum[x1][y1] += degree
        skill_sum[x1][y2+1] -= degree
        skill_sum[x2+1][y1] -= degree
        skill_sum[x2+1][y2+1] += degree
    
    for i in range(n):
        for j in range(m):
            skill_sum[i][j+1] += skill_sum[i][j]  # 가로 방향 누적 합
    for j in range(m):
        for i in range(n):
            skill_sum[i+1][j] += skill_sum[i][j]  # 세로 방향 누적 합
    
    for i in range(n):
        for j in range(m):
            if board[i][j] + skill_sum[i][j] > 0:
                answer += 1
    
    return answer