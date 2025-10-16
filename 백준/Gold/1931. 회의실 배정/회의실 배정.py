import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

n=int(input())
times=[]
for i in range(n):
    s,e=map(int,input().split())
    times.append((s,e))

# 끝나는 시간을 기준으로 오름차순 정렬   
times.sort(key=lambda x: (x[1],x[0]))

et=0
cnt=0

for s,e in times:
    #끝나는 시간보다 시작 시간이 뒤면
    if et<=s:
        et=e
        cnt+=1
print(cnt)        