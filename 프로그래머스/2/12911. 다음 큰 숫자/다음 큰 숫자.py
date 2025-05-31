def solution(n):
    n_one_count: int = format(n, 'b').count('1')
    num: int = n + 1
    while True:
        num_one_count: int = format(num, 'b').count('1')
        if n_one_count == num_one_count:
            return num
        num += 1
    
    return num