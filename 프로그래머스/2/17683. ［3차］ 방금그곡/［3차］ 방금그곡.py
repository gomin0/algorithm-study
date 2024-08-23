def replace_sharps(melody):
    melody = melody.replace("C#", "c")
    melody = melody.replace("D#", "d")
    melody = melody.replace("F#", "f")
    melody = melody.replace("G#", "g")
    melody = melody.replace("A#", "a")
    melody = melody.replace("B#", "b") # 슈발 이거는 조건에 없는데 12개만 쓴다며 근데 34테스트 뭐임?
    return melody
def solution(m, musicinfos):
    answer = ''
    music_list = []
    
    for i in musicinfos:
        start, end, title, melody = i.split(",")
        sh, sm = start.split(":")
        eh, em = end.split(":")
        time = int(eh)*60 + int(em) - (int(sh)*60 + int(sm))

        melody = replace_sharps(melody)
        m = replace_sharps(m)
        music = ""
        
        for j in range(time):
            music += melody[j%len(melody)]

        if m in music:
            music_list.append((title, time, start))

    length = len(music_list)
    if length == 0:
        return "(None)" # 이것도 좀.. ㅋㅋ
    elif length == 1:
        return music_list[0][0]
    else:
        music_list.sort(key=lambda x: (-x[1], x[2]))
        return music_list[0][0]
          
    return answer