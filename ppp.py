import sys

try :
    sys.stdin = open("test.inp", "r")
    sys.stdout = open("test.out", "w")
except :
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

while True :
    try : 
        t, a, b = map(int, input().split())
    except EOFError :
        break
    
    a = t**a - 1
    b = t**b - 1
    
    if (b == 0 or a % b != 0) :
        print("is not an integer with less than 100 digits.")
    else :
        P = int(a / b)
        p = P
        cnt = 0
        while (P != 0) :
            cnt += 1
            P //= 10
        if (cnt < 100) :
            print(p) 
        else :
            print("is not an integer with less than 100 digits.") 