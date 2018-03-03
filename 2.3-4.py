import os


def recursiveInsertionSort(Arr):
	#condition for stop repeating
	if len(Arr) <= 1:
		return Arr
	#make 1-element short array, sort it recursively and put element that separated just before in array
	NewArr = Arr[0:len(Arr)-1]
	NewArr = recursiveInsertionSort(NewArr)
	NewArr = NewArr + [Arr[len(Arr)-1]]
	return doSort(NewArr)


def doSort(Arr):
	#put a new element into the sorted area
	key = Arr[len(Arr)-1]
	i = len(Arr) - 2
	while i>(-1) and Arr[i]>key:
		Arr[i+1] = Arr[i]
		i = i - 1
	Arr[i+1] = key
	return Arr

	
A = [15,111,20,33,1,0,55]
print(recursiveInsertionSort(A))

B = [ 1, 2, 2 , 14, 33, -34, 3, 5, 45,  54, 0 , 96]
print(recursiveInsertionSort(B))

