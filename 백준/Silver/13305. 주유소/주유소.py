#import sys
#sys.stdin=open("input.txt",'r')

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

min_cost=b[0]
tot=0

for i in range(n-1):
    if min_cost>b[i]:
        min_cost=b[i]
    tot+=a[i]*min_cost

print(tot)