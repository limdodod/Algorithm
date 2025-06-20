T=int(input())

for i in range(T):
    A,B=input().split()
    A=int(A)
    result=''
    for char in B:
        result+=char*A
    print(result)