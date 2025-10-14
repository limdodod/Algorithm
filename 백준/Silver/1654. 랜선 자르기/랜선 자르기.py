#import sys
#sys.stdin=open("input.txt",'r')
def Count(len):
   cnt=0
   for x in a: 
       cnt+=(x//len) 
   
   return cnt
   


k,n=map(int,input().split())
a=[]
largest=0
for _ in range(k):
   x=int(input())
   a.append(x)
   largest=max(x,largest)

lt=1
rt=largest
res=0

while lt<=rt:
   mid=(lt+rt)//2
   if Count(mid)>=n:
      res=mid
      lt=mid+1
   else:
      rt=mid-1
      
print(res)