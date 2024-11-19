N = int(input())
arr = list(map(int, input().split()))
current_absent_days = 0
max_absent_days = 0
for day in arr:
    if day == 0:
        current_absent_days += 1
        max_absent_days = max(max_absent_days,current_absent_days)
    else:
        current_absent_days = 0
print(max_absent_days)
