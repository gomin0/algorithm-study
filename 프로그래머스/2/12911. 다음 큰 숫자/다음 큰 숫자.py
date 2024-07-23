def solution(n):
    for i in range(n + 1, 1000001):
        if bin(i).count('1') == bin(n).count('1'):
            return i