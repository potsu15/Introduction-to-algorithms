import os


def linear(A):
	max = A[0]
	tmp = A[0]
	start = 0
	end = 0
	tmp_start = 0
	tmp_end = 0
	for i in range(1,len(A)):
		if A[i] > A[i] + tmp:
			tmp = A[i]
			tmp_start = i
			tmp_end = i
		else:
			tmp = tmp + A[i]
			tmp_end = i
		if tmp >= max:
			max = tmp
			start = tmp_start
			end = tmp_end
	return [start,end,max]
	
	
print(linear([0,0,0,0,-1,1,1,1,-1,0,0,0,0]))
print(linear([1,1,1,1,0,-50,0,-1,1,1,1,1,1,1,-1,0,0]))