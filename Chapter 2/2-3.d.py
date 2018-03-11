import os


def simple( coefficientlist , x ):
	sum = 0
	for i in range ( 0 , len(coefficientlist) ):
		sum = coefficientlist[ len(coefficientlist) - i - 1 ] + x*sum
	return sum
	
print(simple([1,1,1,1,1],3))

print(simple([1,-1,1,-1,1],2))

