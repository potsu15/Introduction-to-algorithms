import os


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
			return a
		else:
			if A[mid] < key:
				return binarySearch( A , mid + 1 , b , key )
			else:
				return binarySearch( A , a , mid - 1 , key )
		
		
def sort(A):
    for j in range(1,len(A)):
        key = A[j]
        keyindex = binarySearch( A , 0 , len(A)-1 , key )
        if A[keyindex] > key:
            keyindex = keyindex - 1
        i = j - 1
        while i>(-1) and i>keyindex:
            A[i+1] = A[i]
            i= i -1
        A[i+1] = key
    return A

B = [ 5, 3, 20 ,33, 14 ,444,-3 ,-3,-3,  -2, -1]
print(sort(B))