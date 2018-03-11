import os


def simple( coefficientlist , x ):
	sum = 0
	for i in range( 0 , len(coefficientlist) ):
		term = coefficientlist[i]
		for j in range ( 0 , i ):
			term = term*x
		sum = sum + term
	return sum
	
print(simple([1,1,1,1,1],3))

print(simple([1,-1,1,-1,1],2))
