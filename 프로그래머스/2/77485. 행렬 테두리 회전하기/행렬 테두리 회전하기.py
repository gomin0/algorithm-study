def solution(rows, columns, queries):
    answer = []
    
    matrix = [[0] * columns for _ in range(rows)]
    
    num = 1
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = num
            num += 1
    
    for x1, y1, x2, y2 in queries:
        prev_value = matrix[x1-1][y1-1]  # 좌상단 값
        min_value = prev_value
        
        # 왼쪽 테두리
        for i in range(x1-1, x2-1):
            matrix[i][y1-1] = matrix[i + 1][y1-1] # 올리기
            min_value = min(min_value, matrix[i][y1-1])
            
        # 아래쪽 테두리
        for i in range(y1-1, y2-1):
            matrix[x2-1][i] = matrix[x2-1][i + 1] # 왼쪽으로
            min_value = min(min_value, matrix[x2-1][i])
            
        # 오른쪽 테두리
        for i in range(x2-1, x1-1, -1):
            matrix[i][y2-1] = matrix[i - 1][y2-1] # 내리기
            min_value = min(min_value, matrix[i][y2-1])
        
        # 위쪽 테두리
        for i in range(y2-1, y1-1, -1):
            matrix[x1-1][i] = matrix[x1-1][i - 1] # 오른쪽으로
            min_value = min(min_value, matrix[x1-1][i])
        
        # 시작점 옮기기
        matrix[x1-1][y1] = prev_value
        
        answer.append(min_value)

    
    return answer