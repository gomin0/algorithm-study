from collections import defaultdict

def solution(gems):
    answer: list[int] = [0, len(gems)-1]
    
    gem_types: int = len(set(gems))
    gem_dict: defaultdict[str, int] = defaultdict(int)
    
    i: int
    j: int
    i = j = 0
    while j < len(gems):
        gem_dict[gems[j]] += 1
        while len(gem_dict) == gem_types:
            if (answer[1] - answer[0]) > j - i:
                answer = [i, j]
            gem_dict[gems[i]] -= 1
            if gem_dict[gems[i]] == 0:
                del gem_dict[gems[i]]
            i += 1
        j += 1
    
    return [answer[0] + 1, answer[1] + 1]