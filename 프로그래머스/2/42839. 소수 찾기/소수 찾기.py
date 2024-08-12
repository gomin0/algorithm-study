import itertools
import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False 
    return True

def solution(numbers):
    answer = 0
    num_set = set()
    
    for j in range(1, len(numbers) + 1):
        # 숫자의 모든 조합을 생성
        for comb in itertools.permutations(numbers, j):
            num_set.add(int(''.join(comb)))
            
    for k in num_set:
        if is_prime(k):
            answer += 1
        
    return answer