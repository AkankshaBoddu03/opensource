N = int(input())
arr = list(map(int, input().split()))
balance_arr = []
total_sum = sum(arr)
left_weight = 0
for i in range(N):
    right_weight = total_sum - left_weight - arr[i]
    bal_val = abs(left_weight - right_weight)
    balance_arr.append(bal_val)
    left_weight += arr[i]
print(" ".join(map(str,balance_arr)))
