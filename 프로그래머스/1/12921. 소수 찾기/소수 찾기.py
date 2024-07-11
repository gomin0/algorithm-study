def solution(n):
    primes = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n + 1):
        if primes[p]:
            prime_numbers.append(p)
    return len(prime_numbers)

# 시간 초과
# def is_prime(n):
#     count = 0
#     for i in range(1, int(n ** 0.5) + 1):
#         if i ** 2 == n:
#             count += 1
#         elif n % i == 0:
#             count += 2
#     return count == 2

# def solution(n):
#     answer = 0
#     for i in range(1, n + 1):
#         if is_prime(i):
#             answer += 1
#     return answer