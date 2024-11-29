from itertools import permutations

def solution(n, weak, dist):
    answer = float('inf')
    
    length = len(weak)
    extended_weak = weak + [w + n for w in weak]
    
    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start
            
            for friend in friends:
                position += friend
                if position < extended_weak[i+length - 1]: # 마지막에 도달 못함
                    count += 1
                    position = [w for w in extended_weak[i+1:i+length] if w > position][0]
                else:
                    answer = min(answer, count)
                    break
    
    return answer if answer != float('inf') else -1