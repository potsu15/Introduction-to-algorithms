import os


#global variable that counts the number of inversions
global invcount
invcount = 0
	
	
def merge(A,p,q,r):

	global invcount
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
			invcount += n1 - i
			A[k] = R[j]
			j = j + 1
	#case of when list L is completely copied to A
	if i == n1:
		for l in range( k , r + 1 ):
			A[l] = R[j]
			j = j + 1
	#case of when list R is completely copied to A
	else:
		for l in range ( k , r + 1 ):
			A[l] = L[i]
			i = i + 1
	return A

	
def mergeCount(A,p,r):
	global invcount
	if p < r:
		q = int((p+r)/2)
		mergeCount(A,p,q)
		mergeCount(A,q+1,r)
		merge(A,p,q,r)

	return invcount


	
A = [15,111,20,33,1,0,55]
print(mergeCount(A,0,6))
invcount = 0
B = [23, -1, 0, 2.3 , 223 , 1, 43 ,34 ,44, 33 , 5]
print(mergeCount(B,0,10))
