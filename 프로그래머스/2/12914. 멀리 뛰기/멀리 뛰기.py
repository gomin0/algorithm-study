def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    jump_bound: list[int] = [0] * (n+1)
    jump_bound[1] = 1
    jump_bound[2] = 2

    for i in range(3, n + 1):
        jump_bound[i] = jump_bound[i-1] + jump_bound[i-2]
    
    return jump_bound[n] % 1234567