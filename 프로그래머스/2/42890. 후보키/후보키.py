from itertools import combinations

def solution(relation):    
    row = len(relation)
    col = len(relation[0])
    
    # 모든 컬럼 조합
    comb = []
    for i in range(1, col + 1):
        comb.extend(combinations(range(col), i))
    
    # 유일성
    unique = []
    u = set()
    for c in comb:
        temp = []
        for r in relation:
            key = ''
            for k in c:
                key += r[k]
            temp.append(key)
        if len(set(temp)) == row:
            unique.append(set(c))

    # 최소성
    answer = []
    for u in unique:
        is_minimal = True  # 최소성을 만족하는지 체크하는 플래그
        for x in answer:
            is_subset = True
            # x의 모든 요소가 u에 포함되어 있는지 확인
            for elem in x:
                if elem not in u:
                    is_subset = False
                    break
            if is_subset:  # x가 u의 부분집합이면 최소성 불만족
                is_minimal = False
                break
        if is_minimal:
            answer.append(u)
    
    
    return len(answer)