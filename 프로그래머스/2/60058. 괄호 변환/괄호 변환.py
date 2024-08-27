def correct(p):
    c = 0
    for parentheses in p:
        if c < 0:
            return False
        if parentheses == '(':
            c += 1
        else:
            c -= 1
    if c == 0:
        return True
    else:
        return False

# 4-4
def changeU(u):
    newU = u[1:-1]
    reverseU = ''
    for char in newU:
        if char == '(':
            reverseU += ')'
        else:
            reverseU += '('
    return reverseU

def solution(p):
    
    # 1.
    if p == '':
        return p
    
    # 이미 올바른 괄호면 그대로 return
    if correct(p):
        return p
    
    u = ''
    v = ''
    balance = 0
    
    # 2.
    for i in range(len(p)):
        if i != 0 and balance == 0:
            v = p[i:]
            break
        if p[i] == '(':
            balance += 1
            u += '('
        else:
            balance -= 1
            u += ')'
    
    if correct(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        answer += changeU(u)
        return answer