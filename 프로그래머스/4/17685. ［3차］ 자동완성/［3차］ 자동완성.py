def solution(words):
    answer: int = 0
    words.sort()
    
    for i, word in enumerate(words):
        prev: int = 0
        next: int = 0
        if i > 0:
            prev = common_prefix(words[i-1], word)
        if i < len(words) - 1:
            next = common_prefix(words[i+1], word)
        
        need: int = max(prev, next) + 1
        answer += min(len(word), need)
    
    return answer


def common_prefix(w1, w2):
    count: int = 0
    for x, y in zip(w1, w2):
        if x == y:
            count += 1
        else:
            break
    return count