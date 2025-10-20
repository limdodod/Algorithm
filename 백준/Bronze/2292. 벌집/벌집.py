import sys

n=int(input())

last=1
cnt=1

while n>last:
    last+=6*cnt
    cnt+=1

print(cnt)
