def solution(s, skip, index):
    
    answer = ""
    
    alpha = ['a', 'b', 'c', 'd', 'e', 'f' , 'g', 'h', 'i', 'j' ,'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for sk in skip:
        alpha.remove(sk)
    
    for i in s:
        new_alpha = (alpha.index(i) + index) % len(alpha)
        answer += alpha[new_alpha]
    
    return answer