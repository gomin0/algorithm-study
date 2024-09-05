def solution(n):
    def move(n, start, end, temp, moves):
        if n == 1:
            moves.append([start, end])
        else:
            # 1. 가장 큰거 빼고 n-1개 2로 옮김
            move(n-1, start, temp, end, moves)
            # 2. 가장 큰거 3으로 옮김
            moves.append([start, end])
            # 3. n-1개 2에서 3으로 옮기기
            move(n-1, temp, end, start, moves)
    
    moves = []
    move(n, 1, 3, 2, moves)
    return moves