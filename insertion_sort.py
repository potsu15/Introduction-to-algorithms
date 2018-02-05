import os
def sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i>(-1) and A[i]>key:
            A[i+1] = A[i]
            i= i -1
        A[i+1] = key
    return A
	
A = [15,111,20,33,1,0,55]
sort(A)
print(A)