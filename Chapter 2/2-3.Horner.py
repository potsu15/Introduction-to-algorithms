import os


# A is list of coefficients
def Horner(A,x):
	y = 0
	for i in range(0, len(A)):
		y = A[len(A)-i-1] + x*y
	return y
	
	
print(Horner([1,2,3],2))
