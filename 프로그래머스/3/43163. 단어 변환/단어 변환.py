from collections import deque

def check_convertable(word1, word2):
    diff: int = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff += 1
    return diff == 1


def solution(begin, target, words):
    answer: int = 0
    
    def bfs(start):
        queue: list[str] = deque([(start, 0)])
        visited.add(start)
        
        while queue:
            now: str
            step: int
            now, step = queue.popleft()
            if now == target:
                return step
            
            for word in words:
                if word not in visited and check_convertable(now, word):
                    visited.add(word)
                    queue.append((word, step + 1))
        return 0
    
    visited: set[str] = set()
    answer = bfs(begin)
    
    return answer