def solution(book_time):
    answer = 0
    book_time.sort()
    room = []
    
    # 이렇게 하면 10분 더했을 때 60분이 넘어가면 시를 올려줘야하는데 문제발생
    # for book in book_time:
    #     start = int(book[0].replace(':', ''))
    #     end = int(book[1].replace(':', '')) + 10  # 청소시간까지
    
    # 다 분으로 바꿔
    for book in book_time:
        start_h, start_m = book[0].split(':')
        start = int(start_h) * 60 + int(start_m)
        end_h, end_m = book[1].split(':')
        end = int(end_h) * 60 + int(end_m) + 10
        
        possible = False
        for i in range(len(room)):
            if room[i] <= start:
                room[i] = end
                possible = True  # 들어갈 수 있는 방 탐색
                break
        if not possible:
            room.append(end)  # 방 추가
    
    return len(room)