M=int(input())
N=int(input())

list=[]

for i in range(M,N+1):
    for x in range(2,i+1):
        if i%x==0:
            if i==x:
                list.append(i)
            break

if list:
    print(sum(list))
    print(min(list))
else:
    print("-1")
                