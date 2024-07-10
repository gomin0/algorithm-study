def solution(sizes):
    answer = 0
    
    row = []
    column = []
    
    for i in range(len(sizes)):
        row.append(max(sizes[i][0], sizes[i][1]))
        column.append(min(sizes[i][0], sizes[i][1]))
    
    answer = max(row) * max(column)
    
    return answer