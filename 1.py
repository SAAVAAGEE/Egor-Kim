s=[]

for i in range(10):
	i=int(input("\n������� ������� �������: "))
	s.append(i)

element=max(s)
print('���������� ������� �������:',element)

for i in s:
    	if i>element:
		print(i,">",element)
    	elif i<element:
		print(i,"<",element)
    	elif i==element:
	 	print(i,"<",element)
