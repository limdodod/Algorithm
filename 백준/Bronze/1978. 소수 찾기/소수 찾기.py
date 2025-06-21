N=int(input())
nums=list(map(int,input().split()))

count=0
for i in nums:
    for x in range(2,i+1):
        if i%x==0:
            if i==x:
                count +=1
        
            break
            
print(count)
    