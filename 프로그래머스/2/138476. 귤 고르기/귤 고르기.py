def solution(k, tangerine):
    answer = 0
    tangerine_count = {}
    for i in tangerine:
        if i in tangerine_count:
            tangerine_count[i] += 1
        else:
            tangerine_count[i] = 1
    
    sorted_tangerine = sorted(tangerine_count.values(), reverse=True)
    
    for j in sorted_tangerine:
        k -= j
        answer += 1
        if k <= 0:
            return answer
    return answer