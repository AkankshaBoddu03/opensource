n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_num1 = 0
sum_num2 = 0
for i in range(0,n):
    if arr[i] % m == 0:
        sum_num1 += arr[i]
    else:
        sum_num2 += arr[i]
print(sum_num1 - sum_num2)
