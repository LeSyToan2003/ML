import sys

try :
    sys.stdin = open("test.inp", "r")
    sys.stdout = open("test.out", "w")
except :
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

###### NHẬP NHIỀU DÒNG ######
# while True :
#     try : 
#         s = input()
#     except EOFError :
#         break
#     print(s)

###### KIỂM TRA KIỂU DỮ LIỆU ######
# s1 = (1,3,4)
# s2 = [1,2,3,4,5]
# s3 = "aaaa"
# print(type(s1))

###### CHUYỂN HỆ CƠ SỐ ######
# a = -42
# b = hex(a)[2:]
# c = bin(a)[2:]
# print(b)

###### HÀM PRINT ######
# print("abc", "dfe")
# print("abc", end = " - ")
# print("aaa")
# print("\"abc\"")

###### STRING ######
# s = "abc"
# print(s[1:3])
# print(s[2:])

###### IF ELSE ######
# a, b, c = 2, 3, 3
# if (not (a == 1 or b == 2)) :
#     print(c)

###### TOÁN TỬ ######
# a, b, c = 1, 3, 4
# d = c // b
# e = c ** b
# print(e)