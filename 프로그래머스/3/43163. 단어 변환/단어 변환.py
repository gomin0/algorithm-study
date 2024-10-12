from collections import deque

def word_diff(word1, word2):
    diff_count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            diff_count += 1
    return diff_count == 1

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])  # 단어, 변환 수
    visited = set([begin])
    
    while queue:
        word, count = queue.popleft()
        
        if word == target:
            return count
        
        for w in words:
            if w not in visited and word_diff(word, w):
                visited.add(w)
                queue.append((w, count + 1))

    return 0