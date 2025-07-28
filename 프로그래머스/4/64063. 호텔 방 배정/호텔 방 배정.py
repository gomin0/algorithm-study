def solution(k, room_number):
    next_room = {}

    def find(room):
        path = []
        while room in next_room:
            path.append(room)
            room = next_room[room]
        for r in path:
            next_room[r] = room
        return room

    answer = []
    for room in room_number:
        available = find(room)
        answer.append(available)
        next_room[available] = find(available + 1)
    
    return answer
