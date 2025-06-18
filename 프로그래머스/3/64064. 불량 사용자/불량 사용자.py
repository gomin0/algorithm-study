def is_banned(uid, bid) -> bool:
    if len(uid) != len(bid):
        return False
    for u, b in zip(uid, bid):
        if u != b and b != '*':
            return False
    return True

def solution(user_id, banned_id) -> int:
    result_set: set[tuple[str, ...]] = set()
    visited = [False] * len(user_id)

    def dfs(depth, path) -> None:
        if depth == len(banned_id):
            result_set.add(tuple(sorted(path)))
            return
        for i, uid in enumerate(user_id):
            if visited[i]:
                continue
            if is_banned(uid, banned_id[depth]):
                visited[i] = True
                dfs(depth + 1, path + [uid])
                visited[i] = False

    dfs(0, [])
    return len(result_set)