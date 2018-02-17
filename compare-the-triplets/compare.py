'''
def listsum(numList):

    if len(numList) == 1:
        return numList[0]
    else:
    	print numList[0] ,numList[1:]
    	return numList[0] + listsum(numList[1:])

    	

print(listsum([1,3,5,7,9]))

'''

#!/bin/python

import sys

def solve(A,B):
  	bob = 0
  	alice = 0
 	for i in xrange(0,3):

 		if A[i] > B[i]:
 			alice = alice + 1
 		elif A[i] < B[i]:
 			bob = bob + 1

 	print bob, alice

def main():
	a0 = 5
	a1 = 6
	a2 = 7
	A = [int(a0), int(a1), int(a2)]

	b0 = 3
	b1 = 6
	b2 = 10
	B = [int(b0), int(b1), int(b2)]	
	
	obj = solve(A,B)

if __name__ == '__main__':
	main()


