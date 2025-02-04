def solution(n):
    count = 0
    stack = [(0, [], [0] * n, [0] * (2 * n - 1), [0] * (2 * n - 1))]  
    # (현재 행 y, 현재까지 놓인 퀸의 열 리스트, 열 체크 배열, 대각선 체크 배열 2개)

    while stack:
        y, queens, col, diag1, diag2 = stack.pop()

        # 모든 행에 퀸을 놓았을 경우 해답 1개 추가
        if y == n:
            count += 1
            continue
        
        for x in range(n):
            if col[x] + diag1[x+y] + diag2[x-y+n-1] == 0:
                # 새로운 상태를 스택에 추가 (백트래킹)
                new_col = col[:]
                new_diag1 = diag1[:]
                new_diag2 = diag2[:]
                new_col[x] = new_diag1[x+y] = new_diag2[x-y+n-1] = 1
                stack.append((y + 1, queens + [x], new_col, new_diag1, new_diag2))

    return count