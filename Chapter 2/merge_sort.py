import os



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
		print(A)
	return A

	
A = [15,111,20,33,1,0,55]
print(mergeSort(A,0,6))
B = [23, -1, 0, 2.3 , 223 , 1, 43 ,34 ,44, 33 , 5]
print(mergeSort(B,0,10))
			
