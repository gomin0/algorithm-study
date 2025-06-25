from collections import defaultdict

def solution(tickets):
    answer: list[str] = []
    route: defaultdict[str, list[str]] = defaultdict(list)
    
    for ticket in tickets:
        start: str
        end: str
        start, end = ticket
        route[start].append(end)
    
    for key in route:
        route[key].sort(reverse=True)
    
    stack: list[str] = ["ICN"]
    while stack:
        top: str = stack[-1]
        if route[top]:
            stack.append(route[top].pop())
        else:
            answer.append(stack.pop())
    
    return answer[::-1]