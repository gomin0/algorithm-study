def solution(phone_book):
    
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True


# 시간초과
# def solution(phone_book):
    
#     phone_book.sort()
#     for i in range(len(phone_book) - 1):
#         for j in range(i+1, len(phone_book)):
#             if phone_book[j].startswith(phone_book[i]):
#                 return False
    
#     return True