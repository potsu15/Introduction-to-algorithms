import os
import timeit
import numpy as np
import matplotlib.pyplot as plt
import random

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
	
	return [start,end,max]

	
def cross(A,low,mid,high):
	left_sum = (-1)*float('inf')
	sum = 0
	for i in range(low , mid + 1):
		sum = sum + A[mid + low - i]
		if sum > left_sum:
			left_sum = sum
			max_left = mid + low - i
	right_sum = (-1)*float('inf')
	sum = 0
	for j in range( mid + 1 , high + 1 ):
		sum = sum + A[j]
		if sum > right_sum:
			right_sum = sum
			max_right = j
	return [max_left,max_right,left_sum+right_sum]
	
	
def main(A,low,high):
	if high == low:
		return [low,high,A[low]]
	else:
		mid = int((low+high)/2)
		left_case = main(A,low,mid)
		right_case = main(A,mid + 1,high)
		cross_case = cross(A,low,mid,high)
		if left_case[2] >=  right_case[2] and left_case[2] >= cross_case[2]:
			return left_case
		else:
			if right_case[2] >= left_case[2] and right_case[2] >= cross_case[2]:
				return right_case
			else:
				return cross_case


#switching spot is n = 16(array's length)				
def hybrid(A,low,high):
	if high - low <= 15:
		return dumb(A[low:high+1])
	
	if high == low:
		return [low,high,A[low]]
	else:
		mid = int((low+high)/2)
		left_case = hybrid(A,low,mid)
		right_case = hybrid(A,mid + 1,high)
		cross_case = cross(A,low,mid,high)
		if left_case[2] >=  right_case[2] and left_case[2] >= cross_case[2]:
			return left_case
		else:
			if right_case[2] >= left_case[2] and right_case[2] >= cross_case[2]:
				return right_case
			else:
				return cross_case

				
def drawer():
	X = []
	Y = []
	for i in range (1 , 50):
		A = []
		for j in range (0 , i):
			A = A + [random.randrange(-30,30)]
		
		start = timeit.default_timer()
		dumb(A)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='brute force algorithm')

	
def drawer2():
	X = []
	Y = []
	for i in range (1 , 50):
		A = []
		for j in range (0 , i):
			A = A + [random.randrange(-30,30)]
		
		start = timeit.default_timer()
		main(A,0,i-1)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='recursive algorithm')
	
	
def drawer3():
	X = []
	Y = []
	for i in range (1 , 50):
		A = []
		for j in range (0 , i):
			A = A + [random.randrange(-30,30)]
		
		start = timeit.default_timer()
		hybrid(A,0,i-1)
		stop = timeit.default_timer()
		
		X = X + [i]
		Y = Y + [stop - start]
	plt.plot(X,Y,label='hybrid algorithm')	
	

plt.figure		
drawer()
drawer2()
drawer3()
plt.xlabel("array's length")
plt.ylabel("running time")
plt.title("brute force algorithm, recursive algorithm and hybrid algorithm 's running time depend on array's length")
plt.legend(loc='upper left')
plt.show()	