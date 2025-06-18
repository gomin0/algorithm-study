from itertools import permutations

def is_banned(uid, bid) -> bool:
    if len(uid) != len(bid):
        return False
    for u, b in zip(uid, bid):
        if u != b and b != '*':
            return False
    return True

def solution(user_id, banned_id) -> int:
    ban: set[tuple[str, ...]] = set()
    user_case: list[tuple[str, ...]] = list(permutations(user_id, len(banned_id)))
    
    for case in user_case:
        for uid, bid in zip(case, banned_id):
            if not is_banned(uid, bid):
                break
        else:
            ban.add(tuple(sorted(case)))
    
    return len(ban)