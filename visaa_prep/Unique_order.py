def unique_elem(arr):
    seen = set()
    res = []
    for num in arr:
        if num not in seen:
            res.append(num)
            seen.add(num)
    return res
N = int(input())
arr = list(map(int, input().split()))
unique_arr = unique_elem(arr)
print(" ".join(map(str, unique_arr)))
