from collections import defaultdict

def solution(gems):
    answer = [0, len(gems)-1]
    
    gem_dict = defaultdict(int)
    
    gems_type = len(set(gems))
    
    i = j = 0
    while j < len(gems):
        gem_dict[gems[j]] += 1
        
        while len(gem_dict) == gems_type:
            if (answer[1] - answer[0]) > j - i:
                answer = [i, j]
            gem_dict[gems[i]] -= 1
            if gem_dict[gems[i]] == 0:
                del gem_dict[gems[i]]
            i += 1
        j += 1
        
    return [answer[0] + 1, answer[1] + 1]