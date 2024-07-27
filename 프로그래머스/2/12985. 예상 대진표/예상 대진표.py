def solution(n,a,b):
    answer = 0
    game_round = 0
    count = 0
    while 2 ** count < n:
        count += 1
    
    if a > b:
        a, b = b, a
    
    while True:
        if a <= n/2 and b > n/2:
            return count
        elif a <= n/2 and b <= n/2:
            n /= 2
            count -= 1
        elif a > n/2 and b > n/2:
            a -= n/2
            b -= n/2
            n /= 2
            count -= 1