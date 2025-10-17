import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

n=int(input())
a=list(map(int,input().split()))
# 오름차순 정렬
a.sort()

sum=0
total=0
for i in range(len(a)):
    sum+=a[i]
    total+=sum
    
print(total)