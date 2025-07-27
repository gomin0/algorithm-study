from itertools import permutations

def solution(n, weak, dist):
    length: int = len(weak)
    weak = weak + [i + n for i in weak]
    answer = float('inf')
    
    for friends in permutations(dist):
        for start in range(length):
            count = 1
            position = weak[start] + friends[count - 1]
            
            for i in range(start, start + length):
                if weak[i] > position:
                    count += 1
                    if count > len(friends):
                        break
                    position = weak[i] + friends[count - 1]
            else:
                answer = min(answer, count)
    
    return answer if answer != float('inf') else -1