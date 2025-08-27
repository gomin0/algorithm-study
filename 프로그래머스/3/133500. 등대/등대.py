import sys
sys.setrecursionlimit(200000)
from collections import defaultdict

def solution(n, lighthouse):
    light_map = defaultdict(list)
    for a, b in lighthouse:
        light_map[a].append(b)
        light_map[b].append(a)
    dp = [[0, 0] for _ in range(n+1)]
    visited = set()
    def dfs(node):
        visited.add(node)
        dp[node][0] = 0 # 끈 경우
        dp[node][1] = 1 # 킨 경우
        for next_node in light_map[node]:
            if next_node not in visited:
                dfs(next_node)
                dp[node][0] += dp[next_node][1] # 자신 안키면 연결 노드는 무조건 켜야 함
                dp[node][1] += min(dp[next_node][0], dp[next_node][1]) # 자신 키면 연결 노드는 켜도 되고 안켜도 되는 데 최소가 되게
    dfs(1)
    return min(dp[1][0], dp[1][1])