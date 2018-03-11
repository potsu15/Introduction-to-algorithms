import os

def sumarray(A,B):
	n=len(A)
	C=A
	C.append(0)
	for i in range(0,n-1):
		sum = A[n-i-1] + B[n-i-1]
		if sum == 0:
			C[n-i] = 0
		else:
			if sum == 1:
				C[n-i] = 1
			else:
				if sum == 2:
					C[n-i] = 0
					A[n-i-2]+=1
				else:
					C[n-i] = 1
					A[n-i-2]+=1
	sum = A[0] + B[0]
	if sum == 0:
			C[0] = 0
			C[1] = 0
	else:
		if sum == 1:
			C[0] = 0
			C[1] = 1
		else:
			if sum == 2:
				C[0] = 1
				C[1] = 0
			else:
				C[0] = 1
				C[1] = 1
	return C

A = [1,0,1,1,1,1,0,1]
B = [1,1,1,0,0,1,0,1]
C = sumarray(A,B)
print(C)
