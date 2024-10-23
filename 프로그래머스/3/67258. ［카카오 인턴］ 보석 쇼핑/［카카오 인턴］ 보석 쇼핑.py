from collections import defaultdict

def solution(gems):
    n = len(gems)
    answer = [0, n - 1]
    i = j = 0
    gem_dict = defaultdict(int)
    gem_type = len(set(gems))
    
    while j < n:
        gem_dict[gems[j]] += 1
        
        while len(gem_dict) == gem_type:
            if (answer[1] - answer[0]) > j - i:
                answer = [i, j]
            gem_dict[gems[i]] -= 1
            if gem_dict[gems[i]] == 0:
                del gem_dict[gems[i]]
            i += 1
        j += 1
    
    return [answer[0] + 1, answer[1] + 1]