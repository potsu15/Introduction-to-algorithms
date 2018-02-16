import os
def selection_sort( A ):
	for i in range( 0 , len(A) - 1 ):
		min = A[i]
		min_index = i
		#loop for compare A[i] and other list elements
		for j in range( i+1 , len(A) ):
			# if there is any element that is smaller than A[i] memorize value and index
			if min > A[j]:
				min = A[j]
				min_index = j
		#change A[i] to searched smallest value
		temp = A[i]
		A[i] = A[min_index]
		A[min_index] = temp
	return A


B = [ 5,2, 3, 2, 1, 1, 12, -3 ,0 ,4 , 4343, 7 ,6]
C = [ 1.2 , 5 , 3.3 , -3 , 0 , 44 , 34 , 5]
print (selection_sort(B))
print ( selection_sort(C))
	

	
