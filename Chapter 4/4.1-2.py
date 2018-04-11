import os


def dumb(A):
	max = A[0]
	start_index = 0
	end_index = 0
	for i in range( 1 , len(A) + 1 ):
		sum = 0
		start = 0
		end = i - 1
		for k in range ( 0 , i ):
			sum = sum + A[k]
		for j in range ( i , len(A) + 1):
			if max < sum:
				max = sum
				start_index = start
				end_index = end	
			start = start + 1
			end = end + 1
			# to prevent error
			if j == len(A):
				break
			sum = sum - A[j-i] + A[j]
	print(max)
	print(start_index)
	print(end_index)
	return max


dumb([0,0,0,0,0,1,1,1,0,0,0,0,0])

print("-----")

dumb([1,1,1,1,0,-50,0,0,1,1,1,1,1,1,0,0,0]) 