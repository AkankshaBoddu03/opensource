T = int(input())
for i in range(T):
    X, N = map(int, input().split())
    points = X // 10
    score = points * N
    print(score)
