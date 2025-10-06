from collections import defaultdict, deque


def check(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1
    return count == 1


def solution(begin, target, words):
    load = defaultdict(list)
    for w1 in words:
        for w2 in words:
            if w1 == w2:
                continue
            if check(w1, w2):
                load[w1].append(w2)
                load[w2].append(w1)
    for w in words:
        if check(begin, w):
            load[begin].append(w)
    
    visited = set()
    q = deque()
    q.append((begin, 0))
    visited.add(begin)
    while q:
        word, count = q.popleft()
        if word == target:
            return count
        for next_word in load[word]:
            if next_word not in visited:
                q.append((next_word, count + 1))
                visited.add(next_word)
    return 0