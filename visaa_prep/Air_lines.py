import math
X, N = map(int, input().split())
planes_needed = math.ceil(N / 100)
new_planes = max(0, planes_needed-X)
print(new_planes)
