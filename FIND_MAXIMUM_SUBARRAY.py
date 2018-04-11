import os


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

				
print(main([0,0,0,0,-1,1,1,1,-1,0,0,0,0],0,12))
print(main([1,1,1,1,-1,-50,0,-1,1,1,1,1,1,1,-1,0,0],0,16))

