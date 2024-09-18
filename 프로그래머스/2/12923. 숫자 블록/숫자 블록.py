def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            block = 1
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    if i // j <= 10000000:
                        block = i // j
                        break
                    if j <= 10000000:
                        block = j
            answer.append(block)
    
    return answer