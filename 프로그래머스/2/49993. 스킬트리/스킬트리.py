def solution(skill, skill_trees):
    answer = 0
    skill_sequence = []
    
    for s in range(len(skill) - 1, -1, -1):
        skill_sequence.append(skill[s])

    for i in range(len(skill_trees)):
        can = True
        # copy_skill = skill_sequence 이렇게 두 변수가 동일한 리스트를 참조하게 됨
        copy_skill = skill_sequence[:]
        for j in skill_trees[i]:
            if j in copy_skill:
                if j != copy_skill.pop():
                    can = False
                    break
        if can:
            answer += 1
        
    
    return answer