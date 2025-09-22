def solution(k, room_number):
    next_room = dict()
    
    def find(room):
        path = []
        while room in next_room:
            path.append(room)
            room = next_room[room]
        for p in path:
            next_room[p] = room
        return room
        
    answer = []
    for room in room_number:
        r = find(room)
        answer.append(r)
        next_room[r] = find(r+1)
        
    return answer