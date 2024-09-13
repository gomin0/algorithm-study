def solution(n):
    def place_queen(y):
        nonlocal count
        # 마지막 행까지 퀸 놓은 경우
        if y == n:
            count += 1
            return
        
        for x in range(n):
            # 현재 위치(x, y)에 퀸을 놓을 수 있는지 확인
            # col[x]: x열에 퀸이 있는지
            # diag1[x+y]: 왼쪽 위에서 오른쪽 아래 대각선에 퀸이 있는지
            # diag2[x-y+n-1]: 오른쪽 위에서 왼쪽 아래 대각선에 퀸이 있는지
            if col[x] + diag1[x+y] + diag2[x-y+n-1] == 0:
                # 퀸을 놓을 수 있다면 해당 위치를 사용 중이라고 표시
                col[x] = diag1[x+y] = diag2[x-y+n-1] = 1
                
                # 다음 행으로 이동(재귀)
                place_queen(y+1)
                
                # 백트래킹: 이 위치에 퀸을 놓지 않는 경우를 위해 초기화
                col[x] = diag1[x+y] = diag2[x-y+n-1] = 0

    count = 0
    
    # 사용 여부 저장
    col = [0] * n  # 열
    diag1 = [0] * (2*n-1)  # 왼쪽 위에서 오른쪽 아래 대각선
    diag2 = [0] * (2*n-1)  # 오른쪽 위에서 왼쪽 아래 대각선
    
    # 첫 번째 행부터 시작
    place_queen(0)
    
    return count

# 백 트래킹 -> n이 12일 때 시간 초과
# #(row, col)에 퀸을 놓는 것이 유효한지 확인
# def is_valid(chess, row, col):
#     for i in range(row):
#         # 같은 열에 퀸이 있나 확인
#         if chess[i] == col:
#             return False
#         # 대각선에 퀸이 있나 확인(행간의 차이 = 열간의 차이)
#         if abs(chess[i] - col) == abs(i - row):
#             return False
#     return True

# def queen_count(chess, row, n):
    
#     # 마지막 행 까지 성공한 경우
#     if row == n:
#         return 1
    
#     count = 0
#     for col in range(n):
#         if is_valid(chess, row, col):
#             chess[row] = col # (row, col)에 퀸 놓음
#             count += queen_count(chess, row + 1, n) # 다음 행
#             chess[row] = -1 # 퀸 제거
#     return count

# def solution(n):
#     chess = [-1 for _ in range(n)]   
    
#     return queen_count(chess, 0, n)