def solution(board):
    O_count = 0
    X_count = 0
    
    # 1. 개수로 판단
    for b in board:
        O_count += b.count('O')
        X_count += b.count('X')
    
    ox_sum = O_count + X_count
        
    if ox_sum == 0:
        return 1
    elif (O_count + X_count) % 2 == 0:
        if O_count != X_count:
            return 0
    else:
        if O_count != X_count + 1:
            return 0
    
    # 2. 빙고로 판단
    # O 빙고
    for ox in board:
        if ox == "OOO":
            if O_count != X_count + 1:
                return 0
        
    for i in range(len(board)):
        if board[0][i] == 'O' and board[1][i] == 'O' and board[2][i] == 'O':
            if O_count != X_count + 1:
                return 0
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        if O_count != X_count + 1:
            return 0
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        if O_count != X_count + 1:
            return 0
        
    for ox in board:
        if ox == "XXX":
            if O_count != X_count:
                return 0
        
    for i in range(len(board)):
        if board[0][i] == 'X' and board[1][i] == 'X' and board[2][i] == 'X':
            if O_count != X_count:
                return 0
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        if O_count != X_count:
            return 0
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        if O_count != X_count:
            return 0

    return 1


# 1. 개수로 판단
# 홀수개 이면 -> o가 x보다 하나 더 많아야함
# 짝수개 이면 -> o랑 x가 개수 같아야함

# 2. 빙고로 판단
# 선공이 o -> o가 빙고 했으면 x는 o보다 하나 적어야함
# 후공이 x -> x가 빙고 했으면 o는 x랑 개수 같아야함
