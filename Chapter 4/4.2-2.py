import os
import numpy as np


#you should put 2D-list A,B as array type of numpy.py
def strassen(A,B):
	n = len(A)
	if n == 1:
		C=[A[0]*B[0]]
	else:
		#STEP 1
		A11 = A[0:n/2,0:n/2]
		A12 = A[0:n/2,n/2:n]
		A21 = A[n/2:n,0:n/2]
		A22 = A[n/2:n,n/2:n]
		B11 = B[0:n/2,0:n/2]
		B12 = B[0:n/2,n/2:n]
		B21 = B[n/2:n,0:n/2]
		B22 = B[n/2:n,n/2:n]
		#STEP 2
		S1 = B12 - B22
		S2 = A11 + A12
		S3 = A21 + A22
		S4 = B21 - B11
		S5 = A11 + A22
		S6 = B11 + B22
		S7 = A12 - A22
		S8 = B21 + B22
		S9 = A11 - A21
		S10 = B11 + B12
		#STEP 3
		P1 = strassen(A11,S1)
		P2 = strassen(S2,B22)
		P3 = strassen(S3,B11)
		P4 = strassen(A22,S4)
		P5 = strassen(S5,S6)
		P6 = strassen(S7,S8)
		P7 = strassen(S9,S10)
		#STEP 4
		C11 = P5 + P4 - P2 + P6
		C12 = P1 + P2
		C21 = P3 + P4
		C22 = P5 + P1 - P3 - P7
		#COMBINE
		C1 = []
		C2 = []
		C11 = C11.tolist()
		C12 = C12.tolist()
		C21 = C21.tolist()
		C22 = C22.tolist()
		for i in range ( 0, len(C11)):
			C1 = C1 + [C11[i]+C12[i]]
			C2 = C2 + [C21[i]+C22[i]]
		C = C1 + C2
	C = np.array(C)
	return C

print(strassen(np.array([[1,3],[7,5]]),np.array([[6,8],[4,2]])))