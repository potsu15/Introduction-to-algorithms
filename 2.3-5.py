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
		if a == b:
			return None
		else:
			if A[mid] < key:
				return binarySearch( A , mid + 1 , b , key )
			else:
				return binarySearch( A , a , mid - 1 , key )
		
		
A = [1,2,3,4,5,6,7,8,9]
a = binarySearch(A, 0 , 8 , 5)
B = [ -2, -1, 3, 33, 44, 55, 123 , 222 , 223 ,224 ,224 , 225 ,228]
print (a)
print (binarySearch(B, 0 , 12 , -2))
print (binarySearch(B, 0 , 12 , 3))
print (binarySearch(B, 0 , 12 , 228))	
print (binarySearch(B, 0 , 12 , 5))	
C = [-66, -45, -6, -5, -3, -2, 0, 3, 4, 5, 6, 11, 66]
print (binarySearch(C, 0 , len(C)-1 , 22))	