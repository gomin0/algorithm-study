from collections import Counter

def solution(a):
    n: int = len(a)
    if n == 1:
        return 0
    if n == 2:
        return 2
    
    answer: int = 0
    counter = Counter(a)
    for key in counter:
        if counter[key] * 2 <= answer:
            continue
        
        count: int = 0
        i: int =  0
        while i < n - 1:
            if (a[i] == key or a[i+1] == key) and a[i] != a[i+1]:
                count += 2
                i += 1
            i += 1
        answer = max(answer, count)
    
    return answer