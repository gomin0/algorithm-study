from collections import defaultdict

def solution(tickets):
    answer = []
    
    path = defaultdict(list)
    
    for a, b in tickets:
        path[a].append(b)
    
    for key in path:
        path[key].sort(reverse=True)
    
    def dfs(start):
        while path[start]:
            next_start = path[start].pop()
            dfs(next_start)
        answer.append(start)
    
    dfs('ICN')
    
    return answer[::-1]