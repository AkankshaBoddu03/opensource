A = int(input())
if A < 1 or A > 12:
    print("Invalid")
elif 3 <= A <= 5:
    print("Spring")
elif 6 <= A <= 8:
    print("Summer")
elif 9 <= A <= 11:
    print("Antumn")
else:
    print("Winter")
