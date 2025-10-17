import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

m=input().strip()

# - 를 기준으로 그 뒤는 모두 - 처리
groups = m.split('-')

#첫번째 그룹 합
total = sum(map(int, groups[0].split('+')))

#나머지 그룹 빼기
for g in groups[1:]:
    total -= sum(map(int, g.split('+')))

print(total)