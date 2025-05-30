def solution(A,B):
    length: int = len(A)
    A.sort()
    B.sort(reverse=True)

    answer: int = 0
    for i in range(length):
        answer += A[i] * B[i]

    return answer