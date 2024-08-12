def Quad(arr, x, y, size):
    start = arr[x][y]
    same = True
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != start:
                same = False
                break
        if not same:
            break
    if same:
        return [1, 0] if start == 0 else [0, 1]
    else:
        half_size = size // 2
        top_left = Quad(arr, x, y, half_size)
        top_right = Quad(arr, x, y + half_size, half_size)
        bottom_left = Quad(arr, x + half_size, y, half_size)
        bottom_right = Quad(arr, x + half_size, y + half_size, half_size)
    return [
            top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0],
            top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1]
        ]
    

def solution(arr):
    answer = []
    size = len(arr)
    
    return Quad(arr, 0, 0, size)