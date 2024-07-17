def solution(ingredient):
    answer = 0
    
    stack = []
    burger = [1, 2, 3, 1]
    
    for i in ingredient:
        stack.append(i)
        
        if len(stack) >= 4 and stack[-4:] == burger:
            answer += 1
            # stack = stack[:-4]  # 시간초과
            for _ in range(4):
                stack.pop()
    return answer