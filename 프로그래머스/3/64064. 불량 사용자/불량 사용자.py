from itertools import permutations

def check(uid, bid):
    if len(uid) != len(bid):
        return False
    for u, b in zip(uid, bid):
        if u != b and b != '*':
            return False
    return True

def solution(user_id, banned_id):
    
    ban_list = set()
    
    for up in permutations(user_id, len(banned_id)):
        possible = True
        for uid, bid in zip(up, banned_id):
            if not check(uid, bid):
                possible = False
                break
        if possible:
        	ban_list.add(tuple(sorted(up)))
    
    return len(ban_list)