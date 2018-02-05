import os
def search(list , value):
	for i in range(0, len(list)):
		if list[i] == value:
			break
		index = i + 1
	if index <= (len(list) - 1):
		return index
	else:
		print("can't find the value")
		return NIL

list = [1,2,3,4,5,6,7,8,9]
a = search(list, 5)
print (a)
	
