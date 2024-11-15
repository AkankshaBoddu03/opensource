N = int(input())
current_num = 1
for row in range(1, N + 1):
    for num in range(current_num, current_num+row):
        print(num, end=" ")
    print()
    current_num += row
