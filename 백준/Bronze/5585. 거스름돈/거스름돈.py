import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt",'r')

price=int(input())
change=1000-price #거스름돈

coins=[500,100,50,10,5,1]
cnt=0

for c in coins:
    cnt+=change//c
    change%=c
    
print(cnt)