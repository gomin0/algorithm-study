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
    
    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        now_word, count = queue.popleft()
        
        if now_word == target:
            return count
        
        for next_word in words:
            if word_diff(next_word, now_word):
                queue.append((next_word, count + 1))
                visited.add(next_word)
    
    return 0