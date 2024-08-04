def isprime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    
    for a in range(3, int(num ** (1/2)) + 1, 2):
        if num % a == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    change = ''
    
    while n > 0:
        change = str(n % k) + change
        n //= k

    prime = ''
    for i in change:
        if i == '0':
            if prime and isprime(int(prime)):
                answer += 1
                prime = ''
            else:
                prime = ''
        else:
            prime += i
    if prime and isprime(int(prime)):
        answer += 1
        
    return answer