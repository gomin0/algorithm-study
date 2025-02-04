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

# def solution(n):
#     count = 0
#     stack = [(0, [], [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1))]  
#     # (현재 행 y, 현재까지 놓인 퀸의 열 리스트, 열 체크 배열, 대각선 체크 배열 2개)

#     while stack:
#         y, queens, col, diag1, diag2 = stack.pop()

#         # 모든 행에 퀸을 놓았을 경우 해답 1개 추가
#         if y == n:
#             count += 1
#             continue
        
#         for x in range(n):
#             if col[x] + diag1[x+y] + diag2[x-y+n-1] == 0:
#                 # 새로운 상태를 스택에 추가 (백트래킹)
#                 new_col = col[:]
#                 new_diag1 = diag1[:]
#                 new_diag2 = diag2[:]
#                 new_col[x] = new_diag1[x+y] = new_diag2[x-y+n-1] = 1
#                 stack.append((y + 1, queens + [x], new_col, new_diag1, new_diag2))

#     return count