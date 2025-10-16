import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

h, s = map(int, input().split())
result = []

heard_set = set() 
for _ in range(h):
    name = input().strip()
    heard_set.add(name)

for _ in range(s):
    name = input().strip()
    if name in heard_set:
        result.append(name)
        
# 사전 순 정렬
result.sort()

# 출력
print(len(result))
for name in result:
    print(name)