"""****************************PASCAL_TRIANGLE V1.1**************************************************"""
from __future__ import print_function # for python version below 3.0, this import is necessary to use that end='' in print function.
def sol(degree):
	'''This function will add list of each element into a single list.'''
	globals()['deg_order']=degree
	globals()['list_ele']=[]
	for i in range(deg_order+1):
		list_ele.append(calc(i)) #append list items in a list
	display() #i called it here so that i dont have to call it in main
def calc(num):
	'''this function will generate list of element in each degree and send them to sol()'''
	ele=[]
	if num==0:
		return [1]
	elif num==1:
		return [1,1]
	else:
		ele.insert(0,1)
		ele.insert(num,1)
		for m in range(1,num):
			ele.insert(m,(list_ele[num-1][m-1]+list_ele[num-1][m]))#inserts element in respective index of list item
		return ele
def display():
	'''this will display the triangle as formatted output of triangle'''
	length_of_last_list=len(' '.join(map(str,list_ele[-1])))
	for i in list_ele:
		row=' '.join(map(str,i))
		while len(row)<length_of_last_list:
			row=' '+row+' '
		print(row)
if __name__=='__main__':
	degree=int(input("Enter the order of Pascal_tri: "))
	sol(degree)


#updated_version_1.1
#author-Dev Parajuli... follow me in instagram- @dev18official
