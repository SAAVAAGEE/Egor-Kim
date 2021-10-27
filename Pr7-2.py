import math
def s(a1, a2, a3, a4, d):
    A = (a1 + a2 + d) // 2
    B = (a3 + a4 + d) // 2
    x = math.sqrt(A * (A - a1) * (A - a2) * (A - d)) + math.sqrt(B * (B - a3) * (B - a4) * (B - d))
    return x
a1 = float(input('¬ведите длину стороны a1: '))
a2 = float(input('¬ведите длину стороны a2: '))
a3 = float(input('¬ведите длину стороны a3: '))
a4 = float(input('¬ведите длину стороны a4: '))
d = float(input('¬ведите длину диагонали d: '))
print('ѕлощадь:', round(s(a1, a2, a3, a4, d)))
