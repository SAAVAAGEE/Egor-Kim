s=[]

for i in range(10):
	i=int(input("\nВведите елемент массива: "))
	s.append(i)

element=max(s)
print('Наибольший елемент массива:',element)

for i in s:
    	if i>element:
		print(i,">",element)
    	elif i<element:
		print(i,"<",element)
    	elif i==element:
	 	print(i,"<",element)
