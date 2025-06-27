N = int(input())
x_y = []

for i in range(N): 
    x, y = map(int, input().split())
    x_y.append((x, y))

x_y.sort(key=lambda x: (x[1],x[0]))

for x, y in x_y:
    print(x, y)