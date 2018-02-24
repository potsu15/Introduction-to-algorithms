import os

#main idea of algorithm :: first, sort the list by using merge sort. second , find the value X by using binary_search.
#each use time O(n*ln(n)) , O(n*ln(n)). so entire algorithm is O(n*ln(n))


def merge(A,p,q,r):
	n1 = q - p + 1
	n2 = r - q
	#just use list A to define list
	L = A[:n1]
	R = A[:n2]
	for i in range( 0 , n1 ):
		L[i] = A[p + i]
	for j in range( 0 , n2 ):
		R[j] = A[q + j + 1]
	i = 0
	j = 0
	for k in range( p , r + 1 ):
		# if one of array is completely copied to A, stop comparing
		if i == n1 or j == n2:
			break
		if L[i] <= R[j]:
			A[k] = L[i]
			i = i + 1
		else:
			A[k] = R[j]
			j = j + 1
	#case of when list R is completely copied to A
	if i == n1:
		for l in range( k , r + 1 ):
			A[l] = R[j]
			j = j + 1
	#case of when list L is completely copied to A
	else:
		for l in range ( k , r + 1 ):
			A[l] = L[i]
			i = i + 1
	return A

	
def mergeSort(A,p,r):
	if p < r:
		q = int((p+r)/2)
		mergeSort(A,p,q)
		mergeSort(A,q+1,r)
		merge(A,p,q,r)
		
	return A
	
	
# A is list that already sorted , a and b is each the start and end spot of list , key is value we are searching		
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
			return None
		else:
			if A[mid] < key:
				return binarySearch( A , mid + 1 , b , key )
			else:
				return binarySearch( A , a , mid - 1 , key )
				
				
def mainMethod( S , x ):
	#first sort the list S by using merge sort
	T = mergeSort( S , 0 , len(S) - 1 )
	# choose an one of the element of list S. then search X that satisfy condition by using binarySearch. repeating it n times.
	for i in range( 0 , len(S) - 1 ):
		key = x - S[i]
		y = binarySearch( T , i + 1 , len(S) - 1 , key )
		if y != None:
			print("it exist thou")
			break
	if y == None:
		print("doesn't exist")
		
		
B = [ -2, -1, 3, 33, 44, 55, 123 , 222 , 223 ,224 ,224 , 225 ,228]
mainMethod( B , 1 )
mainMethod( B , 22 )

C = [ 4 , 5 , 3 , 11 , 0 , -2 , -66 , -6 , 6 , 66 , -3 , -45 , -5 ]
mainMethod( C , 22 )
mainMethod( C , 1 )

	
	
		