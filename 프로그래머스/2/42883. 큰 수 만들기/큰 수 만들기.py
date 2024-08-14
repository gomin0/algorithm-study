def solution(number, k):
    answer = ''
    
    num = []
    
    for i in number:
        while num and k > 0 and num[-1] < i:
            num.pop()
            k -= 1
        num.append(i)
    while k > 0:
        num.pop()
        k -= 1
    
    return ''.join(num)