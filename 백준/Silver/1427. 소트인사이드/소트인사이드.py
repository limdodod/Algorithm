N=input()
nums = []

for i in str(N):
    nums.append(int(i))
    
nums.sort(reverse=True) 
 
for i in nums:
    print(i,end='')