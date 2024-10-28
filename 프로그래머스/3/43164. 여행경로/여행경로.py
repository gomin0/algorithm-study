from collections import defaultdict

def solution(tickets):
    answer = []
    
    travel = defaultdict(list)
    
    for start, end in tickets:
        travel[start].append(end)
        
    for key in travel:
        travel[key].sort(reverse=True)
    
    path = []

    def dfs(start):
        while travel[start]:
            next_start = travel[start].pop()
            dfs(next_start)
        path.append(start)
        
    dfs("ICN")
    return path[::-1]