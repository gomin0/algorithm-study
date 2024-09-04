def solution(places):
    answer = []
    
    for i in range(5):
        room = places[i]
        covid = False
        
        for a in range(5):
            if covid:
                break
            for b in range(5):
                if room[a][b] == 'P':
                    if 0 <= a < 5 and 0 <= b - 1 < 5 and room[a][b-1] == 'P':
                        answer.append(0)
                        covid = True
                        break
                    if 0 <= a - 1 < 5 and 0 <= b < 5 and room[a-1][b] == 'P':
                        answer.append(0)
                        covid = True
                        break
                    if 0 <= a < 5 and 0 <= b + 1 < 5 and room[a][b+1] == 'P':
                        answer.append(0)
                        covid = True
                        break
                    if 0 <= a + 1 < 5 and 0 <= b < 5 and room[a+1][b] == 'P':
                        answer.append(0)
                        covid = True
                        break
                    if 0 <= a < 5 and 0 <= b - 2 < 5 and room[a][b - 2] == 'P':
                        if room[a][b-1] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a - 2 < 5 and 0 <= b < 5 and room[a-2][b] == 'P':
                        if room[a-1][b] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a < 5 and 0 <= b + 2 < 5 and room[a][b+2] == 'P':
                        if room[a][b+1] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a + 2 < 5 and 0 <= b < 5 and room[a+2][b] == 'P':
                        if room[a+1][b] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a - 1 < 5 and 0 <= b - 1 < 5 and room[a-1][b-1] == 'P':
                        if room[a-1][b] == 'O' or room[a][b-1] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a - 1 < 5 and 0 <= b + 1 < 5 and room[a-1][b+1] == 'P':
                        if room[a - 1][b] == 'O' or room[a][b+1] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a + 1 < 5 and 0 <= b - 1 < 5 and room[a+1][b-1] == 'P':
                        if room[a+1][b] == 'O' or room[a][b-1] == 'O':
                            answer.append(0)
                            covid = True
                            break
                    if 0 <= a + 1 < 5 and 0 <= b + 1 < 5 and room[a+1][b+1] == 'P':
                        if room[a+1][b] == 'O' or room[a][b+1] == 'O':
                            answer.append(0)
                            covid = True
                            break
        if covid == False:
            answer.append(1)
        
        # a, b 가 있어 맨해튼 거리 2 이하 12 가지 경우
        # a, b - 1        a - 1, b    # 무조건 안됨
        # a, b + 1        a + 1, b    # 무조건 안됨
        # a, b - 2                    # a, b - 1이 x일 때 가능  
        # a - 2, b                    # a - 1, b 가 x 일 때 가능 
        # a, b + 2                    # a, b + 1이 x일 때 가능  
        # a + 2, b                    # a + 1, b 가 x 일 때 가능
        # a - 1, b - 1                # a - 1, b 가 x, a, b - 1 이 x 일 때 가능
        # a - 1, b + 1                # a - 1, b 가 x, a, b + 1 이 x 일 때 가능
        # a + 1, b - 1                # a + 1, b 가 x, a, b - 1 이 x 일 때 가능
        # a + 1, b + 1                # a + 1, b 가 x, a, b + 1 이 x 일 때 가능
        
    
    return answer