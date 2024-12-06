def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    idx_a = 0
    idx_b = 0
    
    while idx_b < len(A):
        if A[idx_a] < B[idx_b]:
            answer += 1
            idx_a += 1
        idx_b += 1
    
    return answer