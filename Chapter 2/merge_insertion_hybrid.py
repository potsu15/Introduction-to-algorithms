import os
import timeit
import numpy as np
import matplotlib.pyplot as plt


def sort(A,p,r):
    for j in range(p+1,r+1):
        key = A[j]
        i = j - 1
        while i>(p-1) and A[i]>key:
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

	
def hybridSort(A,p,r,key):
	if p < r:
		if r-p < key:
			sort(A,p,r)
			return A
		
		q = int((p+r)/2)
		hybridSort(A,p,q,key)
		hybridSort(A,q+1,r,key)
		merge(A,p,q,r)
		
	return A

	
	

	
def drawer():
	X = []
	Y = []
	for i in range (1 , 1000):
		A = []
		for j in range (0 , 1000):
			A = A + [1000 - j]
		
		start = timeit.default_timer()
		hybridSort(A,0,999,i)
		stop = timeit.default_timer()
		
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y)

	

plt.figure		
drawer()

plt.show()
