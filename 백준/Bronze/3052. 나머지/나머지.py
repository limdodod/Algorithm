N= []

for i in  range(10):
    A=int(input())
    B=A%42
    if B not in N:
        N.append(B)

print(len(N))