def solution(n):
    three = ''
    
    while n > 0:
        remain = n % 3
        three = str(remain) + three
        n //= 3
        
    reverse_three = three[::-1]
    ten = int(reverse_three, 3)
    return ten