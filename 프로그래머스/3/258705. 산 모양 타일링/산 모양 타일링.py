def solution(n, tops):
    mod = 10007
    # n 번째와 n+1번째 겹치는 부분을 마름모로 먹는지 여부
    a = [0 for _ in range(n)]  # 먹는 경우
    b = [0 for _ in range(n)]  # 먹지 않는 경우

    a[0] = 1  # 먹는 경우에는 경우 무조건 하나(먹는 경우 하나)
    b[0] = 3 if tops[0] else 2

    for k in range(1, n):
        a[k] = a[k-1] + b[k-1]
        if tops[k]:
            b[k] = a[k-1] * 2 + b[k-1] * 3
        else:
            b[k] = a[k-1] + b[k-1] * 2

        a[k] %= mod
        b[k] %= mod

    return (a[-1]+b[-1]) % mod