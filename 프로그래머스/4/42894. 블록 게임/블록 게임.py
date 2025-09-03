def solution(board):
    answer = 0
    n = len(board)
    
    def is_removable(r, c, h, w):
        #(r,c) ~ (r+h-1, c+w-1) 직사각형 영역 확인
        nums = []
        zeros = []
        for i in range(r, r+h):
            for j in range(c, c+w):
                if board[i][j] == 0:
                    zeros.append((i, j))
                else:
                    nums.append(board[i][j])
        
        # 숫자 종류 1 and 숫자 4칸인 경우아니면 불가능
        if len(set(nums)) != 1 or len(nums) != 4:
            return False
        # 위에가 뚫려 있어야 함
        for (i, j) in zeros:
            for up in range(i):
                if board[up][j] != 0:
                    return False
        return True
    
    def remove(r, c, h, w):
        num = None
        for i in range(r, r+h):
            for j in range(c, c+w):
                if board[i][j] != 0:
                    board[i][j] = 0
    
    while True:
        _break = True
        # 2x3
        for r in range(n-1):
            for c in range(n-2):
                if is_removable(r, c, 2, 3):
                    remove(r, c, 2, 3)
                    answer += 1
                    _break = False
        
        # 3x2
        for r in range(n-2):
            for c in range(n-1):
                if is_removable(r, c, 3, 2):
                    remove(r, c, 3, 2)
                    answer += 1
                    _break = False
        
        if _break:
            break
    
    return answer