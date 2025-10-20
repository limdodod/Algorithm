import sys

h,w,n,m=map(int,input().split())
g_cnt=0
s_cnt=0

while w>0:
    w=w-(m+1)
    g_cnt+=1

while h>0:
    h=h-(n+1)
    s_cnt+=1

print(g_cnt*s_cnt)
