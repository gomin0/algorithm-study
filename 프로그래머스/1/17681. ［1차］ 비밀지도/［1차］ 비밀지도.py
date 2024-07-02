def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        # 이진수로 바꾸는 함수 bin, 앞에 2진수임을 나타내는 0b 슬라이싱
        bin_arr1 = bin(arr1[i])[2:].zfill(n)   # n 자리수 맞추게 0으로 채우는 zfill
        bin_arr2 = bin(arr2[i])[2:].zfill(n)
        secret_map = ""
        for j in range(n):
            if bin_arr1[j] == '1' or bin_arr2[j] == '1':
                secret_map += "#"
            else:
                secret_map += " "
        answer.append(secret_map)
        
    
    return answer