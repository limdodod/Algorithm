S=input()
result = [-1]*26

for i in range(len(S)):
    index=ord(S[i])-ord('a')
    if result[index]==-1:
        result[index]= i
        
for num in result:
    print(num, end=' ')