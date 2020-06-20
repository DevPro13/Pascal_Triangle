from __future__ import print_function
def sol(degree):
	globals()['deg_order']=degree
	globals()['list_ele']=[]
	for i in range(deg_order+1):
		list_ele.append(calc(i))
	display()
def calc(num):
	ele=[]
	if num==0:
		return [1]
	elif num==1:
		return [1,1]
	else:
		ele.insert(0,1)
		ele.insert(num,1)
		for m in range(1,num):
			ele.insert(m,(list_ele[num-1][m-1]+list_ele[num-1][m]))
		return ele
def display():
	for i in range(deg_order+1):
		for j in range(i,(deg_order)):
			print(end=' ')
		for k in range(i+1):
			print(list_ele[i][k],end=' ')
			if (k+1)%2==0:
				print(end=' ')
		print("\n",end='')


degree=int(input("Enter the degree of row of Pascal_tri: "))
sol(degree)

