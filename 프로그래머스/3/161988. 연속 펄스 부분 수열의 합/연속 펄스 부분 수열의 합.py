def solution(sequence):
    answer = 0
    
    n = len(sequence)
    
    pulse1 = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(n)]
    pulse2 = [-sequence[i] if i % 2 == 0 else sequence[i] for i in range(n)]
    
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = pulse1[0]
    dp2[0] = pulse2[0]
    
    for i in range(1, n):
        dp1[i] = max(pulse1[i], dp1[i-1] + pulse1[i])
        dp2[i] = max(pulse2[i], dp2[i-1] + pulse2[i])
    
    return max(max(dp1), max(dp2))