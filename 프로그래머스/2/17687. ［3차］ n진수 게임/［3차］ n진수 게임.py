def solution(n, t, m, p):
    
    def convert(number, base):
        if number == 0:
            return '0'
        digits = '0123456789ABCDEF'
        result = ''
        while number:
            result = digits[number % base] + result
            number //= base
        return result
    
    answer = ''
    num = ''
    number = 0
    
    while len(num) < t*m:
        num += convert(number, n)
        number += 1
        
    for i in range(p-1, t*m, m):
        answer += num[i]
    
    
    return answer