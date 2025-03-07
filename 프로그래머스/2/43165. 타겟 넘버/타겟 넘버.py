def solution(numbers, target):
    answer = 0
    
    n = len(numbers)
    
    stack = [(0, 0)]
    
    while stack:
        idx, num = stack.pop()
        if idx == n:
            if num == target:
                answer += 1
        else:
            stack.append((idx+1, num+numbers[idx]))
            stack.append((idx+1, num-numbers[idx]))
    
    return answer