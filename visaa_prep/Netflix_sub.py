A, B, C, X = map(int, input().split())
if A+B >= X:
    print("YES")
elif B+C >= X:
    print("YES")
elif C+A >= X:
    print("YES")
else:
    print("NO")
