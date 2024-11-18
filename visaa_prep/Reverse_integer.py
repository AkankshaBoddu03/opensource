def rev_integer(n):
    INT_MIN,INT_MAX = -2**31,2**31-1

    rev_num = int(str(abs(n))[::-1])
    if n<0:
        rev_num = -rev_num
    if rev_num < INT_MIN or rev_num > INT_MAX:
        return 0
    return rev_num
n = int(input())
print(rev_integer(n))
