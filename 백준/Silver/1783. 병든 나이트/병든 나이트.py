#import sys
#sys.stdin=open("input.txt",'r')

n,m= map(int,input().split())

if n==2:
    if m<7:
        print((m+1)//2)
    elif m>=7:
        print(4)
elif n==1:
    print(1)
elif n>2:
    if m<=4:
        print(m)
    elif 5<=m<=6:
        print(4)
    else:
        print(m-2)
    