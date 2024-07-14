def solution(babbling):

    answer = 0
    speek = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        speeking = 0
        valid = True
        
        while speeking < len(word):
            matched = False
            for sound in speek:
                if word.startswith(sound, speeking) and not word.startswith(sound * 2, speeking):
                    speeking += len(sound)
                    matched = True
                    break
            if not matched:
                valid = False
                break
        
        if valid:
            answer += 1
    
    return answer