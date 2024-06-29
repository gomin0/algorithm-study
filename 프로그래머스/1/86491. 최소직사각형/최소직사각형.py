def solution(sizes):
    answer = 0
    
    row = []
    column = []
    
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            row.append(sizes[i][1])
            column.append(sizes[i][0])
        else:
            row.append(sizes[i][0])
            column.append(sizes[i][1])
    
    answer = max(row) * max(column)
    
    return answer