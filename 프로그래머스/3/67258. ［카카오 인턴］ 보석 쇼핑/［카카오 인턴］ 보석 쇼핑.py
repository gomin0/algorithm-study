def solution(gems):
    n = len(gems)
    gem_type: int = len(set(gems))
    length = float('inf')
    answer = []
    bag = dict()
    left = right = 0
    while right < n:
        if gems[right] in bag:
            bag[gems[right]] += 1
        else:
            bag[gems[right]] = 1
        while len(bag) == gem_type:
            if right - left < length:
                length = right - left
                answer = [left+1, right+1]
            bag[gems[left]] -= 1
            if bag[gems[left]] == 0:
                del bag[gems[left]]
            left += 1
        right += 1
            
    return answer