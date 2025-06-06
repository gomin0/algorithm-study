def solution(s):
    answer: int = 0
    length: int = len(s)
    s *= 2
    
    for i in range(length):
        correct: bool = True
        stack: list[str] = []
        for j in range(i, i+length):
            c: str = s[j]
            if c in "({[":
                stack.append(c)
            else:
                if not stack:
                    correct = False
                    break
                elif c == ')' and stack[-1] != '(':
                    correct = False
                    break
                elif c == '}' and stack[-1] != '{':
                    correct = False
                    break
                elif c == ']' and stack[-1] != '[':
                    correct = False
                    break
                else:
                    stack.pop()
        if correct and not stack:
            answer += 1
            
    return answer