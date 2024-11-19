N = int(input())
arr = list(map(int, input().split()))
arr1 = []
for i in range(1,N):
    arr1.append(arr[i])
arr1.append(arr[0])
print(" ".join(map(str, arr1)))
