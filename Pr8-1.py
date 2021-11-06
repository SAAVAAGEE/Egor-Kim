from random import randint

m=int(input("¬ведите вол-во строк "))
n=int(input("¬ведите вол-во стоблцов "))

print("Ёлементы массива:")
a = [[randint(1,21) for j in range(n)] for i in range(m)]
for i in range(m):
    print(a[i],max(a[i]))
for i in range(n):
    x=[x[i] for x in a]
for j in range(n):
    print(a[j],min(a[j]))
for i in range(m):
    c=[c[j] for c in a]