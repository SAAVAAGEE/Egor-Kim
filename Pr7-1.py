A = int(input())
B = int(input())
while A != 0 and B != 0:
    if A > B:
        A %= B
    else:
        B %= A
gcd = A + B
print(gcd)
