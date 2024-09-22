from itertools import combinations
import bisect  # 이분 탐색

def solution(info, query):
    info_dict = {}
    
    for i in info:
        data = i.split()
        condition = data[:-1]
        score = int(data[-1])
        
        # 조건 별 가능한 모든 경우
        for n in range(5): # -가 들어가는 개수 0 ~ 4개
            for comb in combinations(range(4), n):  # 0~3의 인덱스 중 n개 조합
                temp = condition[:]
                for idx in comb:
                    temp[idx] = '-'
                key = tuple(temp)  # 튜플로 변환: 딕셔너리의 키는 불변만 가능(튜플은 불변)
                
                if key not in info_dict:
                    info_dict[key] = []  # 초기화
                info_dict[key].append(score)
    
    # 키에대한 점수 정렬
    for key in info_dict:
        info_dict[key].sort()
        
    answer = []
    for q in query:
        q = q.replace("and", "").split()
        condition = tuple(q[:-1])
        score = int(q[-1])
        
        if condition in info_dict:
            count = 0
            scores = info_dict[condition]
            
            idx = bisect.bisect_left(scores, score)  # socres에서 score보다 크지 않은 요소가 들어갈 가장 왼쪽 인덱스
            answer.append(len(scores) - idx)
        else:
            answer.append(0)
    return answer