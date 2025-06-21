while True:
    A, B, C = map(int, input().split())
    
    if A == 0 and B == 0 and C == 0:
        break
    
    length = sorted([A, B, C])
    
    if length[2] >= length[0] + length[1]:
        print("Invalid")
        continue
    
    if A == B == C:
        print("Equilateral")
    elif A == B or B == C or A == C:
        print("Isosceles")
    else:
        print("Scalene")
