def solution(players, callings):
    
    player_positions = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        current_position = player_positions[call]
        previous_player = players[current_position - 1]

        players[current_position - 1], players[current_position] = players[current_position], players[current_position - 1]

        player_positions[call] -= 1
        player_positions[previous_player] += 1
    
    return players
    
    
    
    
    # ㅈㄴ 쉬운데? -> 시간초과;;
    # for i in callings:
    #     call_place = players.index(i) # 여기서 시간 잡아먹음
    #     players[call_place - 1], players[call_place] = players[call_place], players[call_place - 1]
    
    return players