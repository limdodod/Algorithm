import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

N=int(input())
a=list(map(int,input().split())) #크레인 무게 제한
a.sort(reverse=True) #무게 제한 내림차순

M=int(input())                   # 박스 수
b=list(map(int,input().split())) # 박스 무게 
b.sort(reverse=True) #박스 무게 내림차순

#무게 제한이 높은 배가 무거운 박스부터 든다.
if b[0] > a[0]:
    print(-1)
    exit()

time = 0
while b:  # 박스가 남아있는 동안
    idx = 0
    new_b = []  # 이번에 못 옮긴 박스만 담을 리스트
    for x in b:
        if idx < N and a[idx] >= x:
            idx += 1  # 크레인이 박스를 하나 들었다
        else:
            new_b.append(x)
    b = new_b
    time += 1

print(time)
