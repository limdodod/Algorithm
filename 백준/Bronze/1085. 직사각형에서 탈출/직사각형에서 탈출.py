x,y,w,h=map(int,input().split())

distance=[x,y,h-y,w-x]
print(min(distance))