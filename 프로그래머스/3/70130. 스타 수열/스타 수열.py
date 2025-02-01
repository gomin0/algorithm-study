from collections import Counter

def solution(a):
    answer = 0
    
    if len(a) < 2:
        return 0
    
    counter = Counter(a)
    
    for key in counter.keys():
        # 현재 숫자의 등장 횟수가 현재까지의 최대 길이의 절반보다 작다면 건너뜀
        if counter[key] * 2 <= answer:
            continue
            
        count = 0
        i = 0
        while i < len(a) - 1:
            if (a[i] == key or a[i+1] == key) and a[i] != a[i+1]:
                count += 2
                i += 1
            i += 1
            
        answer = max(answer, count)
    
    return answer