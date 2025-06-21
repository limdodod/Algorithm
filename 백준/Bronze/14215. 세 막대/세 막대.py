a,b,c=map(int,input().split())

length=sorted([a,b,c])

if length[2]>=length[1]+length[0]:
    length[2]=length[1]+length[0]-1
    
print(sum(length))