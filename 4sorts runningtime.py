import os
import timeit
import numpy as np
import matplotlib.pyplot as plt


def sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i>(-1) and A[i]>key:
            A[i+1] = A[i]
            i= i -1
        A[i+1] = key
    return A
	

def merge(A,p,q,r):
	n1 = q - p + 1
	n2 = r - q
	#just use list A to define list
	L = A[:n1+1]
	R = A[:n2+1]
	for i in range( 0 , n1 ):
		L[i] = A[p + i]
	for j in range( 0 , n2 ):
		R[j] = A[q + j + 1]
	# like pseudo code add infinite at the end of list
	inf = float("inf")
	L[n1] = inf
	R[n2] = inf
	i = 0
	j = 0
	for k in range( p , r + 1 ):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	return A

	
def mergeSort(A,p,r):
	if p < r:
		q = int((p+r)/2)
		mergeSort(A,p,q)
		mergeSort(A,q+1,r)
		merge(A,p,q,r)
		
	return A

	
def sort2(A,p,r):
    for j in range(p+1,r+1):
        key = A[j]
        i = j - 1
        while i>(p-1) and A[i]>key:
            A[i+1] = A[i]
            i= i -1
        A[i+1] = key
    return A
	

def merge2(A,p,q,r):
	n1 = q - p + 1
	n2 = r - q
	#just use list A to define list
	L = A[:n1+1]
	R = A[:n2+1]
	for i in range( 0 , n1 ):
		L[i] = A[p + i]
	for j in range( 0 , n2 ):
		R[j] = A[q + j + 1]
	# like pseudo code add infinite at the end of list
	inf = float("inf")
	L[n1] = inf
	R[n2] = inf
	i = 0
	j = 0
	for k in range( p , r + 1 ):
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	return A

	
def hybridSort(A,p,r,key):
	if p < r:
		if r-p < key:
			sort2(A,p,r)
			return A
		
		q = int((p+r)/2)
		hybridSort(A,p,q,key)
		hybridSort(A,q+1,r,key)
		merge2(A,p,q,r)
		
	return A

	
def binarySearch( A , a , b , key ):
    # n is length of section that we deal with in method
	n = b + a
	mid = int(n/2)
	# compare mid value of section and key value , then call accordingly itself recursively
	if A[mid] == key:
		return mid
	else:
		# need to prevent loop of method 
		if a >= b:
			return a
		else:
			if A[mid] < key:
				return binarySearch( A , mid + 1 , b , key )
			else:
				return binarySearch( A , a , mid - 1 , key )
		
		
def sort3(A):
    for j in range(1,len(A)):
        key = A[j]
        keyindex = binarySearch( A , 0 , len(A)-1 , key )
        if A[keyindex] > key:
            keyindex = keyindex - 1
        i = j - 1
        while i>(-1) and i>keyindex:
            A[i+1] = A[i]
            i= i -1
        A[i+1] = key
    return A	


# drawing insertion sort's graph	
def drawer():
	X = []
	Y = []
	for i in range (1 , 300):
		A = []
		for j in range (0 , i):
			A = A + [i - j]
		
		start = timeit.default_timer()
		sort(A)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='Insertion Sort')


# drawing merge sort's graph	
def drawer2():
	X = []
	Y = []
	for i in range (1 , 300):
		A = []
		for j in range (0 , i):
			A = A + [i - j]
		
		start = timeit.default_timer()
		mergeSort(A,0,i-1)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='Merge Sort')	
	

# drawing merge-insertion hybrid sort's graph	
def drawer3():
	X = []
	Y = []
	for i in range (1 , 300):
		A = []
		for j in range (0 , i):
			A = A + [i - j]
		
		start = timeit.default_timer()
		hybridSort(A,0,i-1,15)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='Insertion-Merge hybrid Sort')		


# drawing insertion uses binary search sort's graph	
def drawer4():
	X = []
	Y = []
	for i in range (1 , 300):
		A = []
		for j in range (0 , i):
			A = A + [i - j]
		
		start = timeit.default_timer()
		sort3(A)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='Insertion Sort with Binary Search')			

	
plt.figure		
drawer()
drawer2()
drawer3()
drawer4()
plt.xlabel("array's length")
plt.ylabel("running time")
plt.title("4 sorts' running time depend on array's length")
plt.legend(loc='upper left')
plt.show()