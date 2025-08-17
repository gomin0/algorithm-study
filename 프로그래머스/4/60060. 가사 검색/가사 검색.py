from collections import defaultdict
import bisect

def solution(words, queries):
    word_dict = defaultdict(list)
    reversed_dict = defaultdict(list)
    for word in words:
        n = len(word)
        word_dict[n].append(word)
        reversed_dict[n].append(word[::-1]) 
    for n in word_dict.keys():
        word_dict[n].sort()
        reversed_dict[n].sort()
    
    answer = []
    for query in queries:
        n = len(query)
        if query[0] == "?":  # 접두사 모름
            left = query[::-1].replace('?', 'a')
            right = query[::-1].replace('?', 'z')
            arr = reversed_dict[n]
        else:  # 접미사 모름
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            arr = word_dict[n]
        
        l = bisect.bisect_left(arr, left)
        r = bisect.bisect_right(arr, right)
        answer.append(r-l)
    
    return answer