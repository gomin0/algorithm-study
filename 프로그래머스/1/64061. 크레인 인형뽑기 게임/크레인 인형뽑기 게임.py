def solution(board, moves):
    answer = 0
    bucket = []
    
    for i in moves:
        pick = 0
        for j in board:
            pick = j[i - 1]
            if pick != 0:
                j[i - 1] = 0
                break
        if pick != 0:
            if bucket and bucket[-1] == pick:
                bucket.pop()
                answer += 2
            else:
                bucket.append(pick)
    
    return answer