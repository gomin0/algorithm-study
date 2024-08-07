def solution(land):
    length = len(land)
    for i in range(1, length):
        # 현재 행의 각 칸을 밟았을 때 얻을 수 있는 최대 점수를 갱신
        for j in range(4):
            land[i][j] += max(land[i-1][(j+1)%4], land[i-1][(j+2)%4], land[i-1][(j+3)%4])
    
    # 마지막 행에서 얻을 수 있는 최대 점수를 반환
    return max(land[length-1])