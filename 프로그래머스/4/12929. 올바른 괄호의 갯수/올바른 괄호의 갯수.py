def solution(n):
    count = 0

    def dfs(open_cnt, close_cnt):
        nonlocal count
        if open_cnt == n and close_cnt == n:
            count += 1
            return
        if open_cnt < n:
            dfs(open_cnt + 1, close_cnt)
        if close_cnt < open_cnt:
            dfs(open_cnt, close_cnt + 1)

    dfs(0, 0)
    return count