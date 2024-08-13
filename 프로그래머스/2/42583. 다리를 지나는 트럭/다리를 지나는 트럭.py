def solution(bridge_length, weight, truck_weights):
    
    bridge = []
    bridge_weight = weight
    time = 0
    while truck_weights or bridge:
        time += 1
        
        if bridge and time - bridge[0][1] == bridge_length:
            bridge_weight += bridge.pop(0)[0]    
        
        if truck_weights and bridge_weight >= truck_weights[0]:
            truck = truck_weights.pop(0)
            bridge.append([truck, time])
            bridge_weight -= truck
        
    return time