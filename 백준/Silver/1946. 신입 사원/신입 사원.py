import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    grades = []
    for _ in range(n):
        s, m = map(int, input().split())
        grades.append((s, m))

    grades.sort()  # 순위 높은 순

    cnt = 0
    smallest = float('inf')  # 순위 낮은 것
    for s, m in grades:
        if m < smallest:
            smallest = m
            cnt += 1
    print(cnt)
