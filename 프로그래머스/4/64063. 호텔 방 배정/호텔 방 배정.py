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
        my_room = find(room)
        answer.append(my_room)
        next_room[my_room] = find(my_room+1)
    return answer
