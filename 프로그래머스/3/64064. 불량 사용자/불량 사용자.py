from itertools import permutations

def match(uid, bid):
    if len(uid) != len(bid):
        return False
    for i in range(len(uid)):
        if uid[i] != bid[i] and bid[i] != '*':
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    
    ban_list = []
    
    for permutation in permutations(user_id, len(banned_id)):
        is_match = True
        for uid, bid in zip(permutation, banned_id):
            if not match(uid, bid):
                is_match = False
                break
        if is_match:
            ban_list.append(tuple(sorted(permutation)))
    
    return len(set(ban_list))