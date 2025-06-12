def solution(A, B):
    answer: int = 0
    A.sort()
    B.sort()
    i: int = 0
    j: int = 0
    
    while j < len(B):
        if A[i] < B[j]:
            i += 1
            answer += 1
        j += 1
        
    return answer