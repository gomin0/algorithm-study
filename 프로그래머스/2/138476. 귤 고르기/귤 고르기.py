from collections import Counter

def solution(k, tangerine):
    answer: int = 0
    tangerine_count: list[tuple] = Counter(tangerine).most_common()
    
    for i in range(len(tangerine_count)):
        if k > 0:
            k -= tangerine_count[i][1]
            answer += 1
        else:
            break

    return answer