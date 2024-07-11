import itertools

def is_prime(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if i ** 2 == n:
            count += 1
        elif n % i == 0:
            count += 2
    return count == 2
    
def solution(nums):
    answer = 0
    for comb in itertools.combinations(nums, 3):
        if is_prime(sum(comb)):
            answer += 1
    return answer