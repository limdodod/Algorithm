A=int(input())
B=int(input())
C=int(input())

if A+B+C != 180:
    print("Error")
elif A==B==C:
    print("Equilateral")
elif A!=B and A!=C and B!=C:
    print("Scalene")
else:
    print("Isosceles")