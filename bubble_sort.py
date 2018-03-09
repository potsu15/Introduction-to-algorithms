import os


def bubble(A):
	for i in range ( 0 , len(A) - 1 ):
		for j in range ( 0 , len(A) -i -1 ):
			if A[j] > A[j+1]:
				tmp = A[j]
				A[j] = A[j+1]
				A[j+1] = tmp
	return A

	
print(bubble([2,3,2,1,55,34,22,15,16,17]))