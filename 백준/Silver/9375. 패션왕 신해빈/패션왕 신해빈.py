n=int(input())
x=0
y=0
result=0
for i in range (n):
    m=int(input())
    clothes={}
    for j in range (m):
        name, kind =input().split()
        if kind in clothes:
            clothes[kind].append(name)
        else:
            clothes[kind]=[name]

    result=1
    for kind in clothes:
        result*=(len(clothes[kind])+1)
    print(result-1)