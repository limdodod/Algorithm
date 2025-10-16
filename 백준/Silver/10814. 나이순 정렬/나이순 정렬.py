import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

n=int(input())
a=[]

for i in range(n):
    age,name=input().split()
    age=int(age)
    a.append((age,name))
# 나이만 정렬, 이름은 입력순 유지
a.sort(key=lambda x:x[0])


for age, name in a:
    print(age, name)