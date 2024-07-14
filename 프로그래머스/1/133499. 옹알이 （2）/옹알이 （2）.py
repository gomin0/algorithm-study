def solution(babbling):
    
    answer = 0
    speek = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        speeking = 0
        prev_sound = ""
        valid = True
        
        while speeking < len(word):
            matched = False
            for sound in speek:
                if word.startswith(sound, speeking):
                    if sound == prev_sound:
                        valid = False
                        break
                    prev_sound = sound
                    speeking += len(sound)
                    matched = True
                    break
            if not matched:
                valid = False
                break
        
        if valid:
            answer += 1
    
    return answer