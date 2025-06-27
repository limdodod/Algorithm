N=int(input())
x_y=[]

for i in range(N):
    x,y=map(int,input().split())
    x_y.append((x,y))

x_y.sort()

for x,y in x_y:
    print(x,y)
    
    