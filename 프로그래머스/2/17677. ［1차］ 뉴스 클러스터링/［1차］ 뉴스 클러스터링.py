def solution(str1, str2):
    answer = 0

    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = []
    str2_set = []
    count = 0
    
    for i in range(1, len(str1)):
        if (str1[i-1] + str1[i]).isalpha():
            str1_set.append(str1[i-1] + str1[i])
    
    for j in range(1, len(str2)):
        if (str2[j-1] + str2[j]).isalpha():
            str2_set.append(str2[j-1] + str2[j])
    
    if not str1_set and not str2_set: # 둘다 공집합
        return 65536
    
    length1 = len(str1_set)
    length2 = len(str2_set)
    
    for k in str1_set:
        if k in str2_set:
            count += 1
            str2_set.remove(k)
    
    answer = count / (length1 + length2 - count)
        
    return int(answer * 65536)