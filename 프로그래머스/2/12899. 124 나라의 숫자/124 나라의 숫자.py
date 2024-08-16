def solution(n):
    answer = []
    
    while n > 0:
        n -= 1
        remainder = n % 3
        if remainder == 0:
            answer.append('1')
        elif remainder == 1:
            answer.append('2')
        else:
            answer.append('4')
        n //= 3

    # 결과를 역순으로 반환
    return ''.join(answer[::-1])