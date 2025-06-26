a, b, c, d, e, f = map(int, input().split())

N = a*e - d*b

if N == 0:
    print("분모가 0")
else:
    x = (c*e - b*f) // N
    y = (a*f - d*c) // N
    print(x, y)
