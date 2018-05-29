import numpy
import sys
"""
Task

	You are given a space separated list of numbers.
	Your task is to print a reversed NumPy array with the element type float.

Input Format
	
	A single line of input containing space separated numbers.

Output Format

	Print the reverse NumPy array with type float.

Sample Input

	1 2 3 4 -8 -10

Sample Output

	[-10.  -8.   4.   3.   2.   1.]

"""


def arrays(arr):
    	# Turn the numbers into array
    result = numpy.array(arr)
    print(result.astype(float)[::-1])


def main():
        # Get value and split ' '
    arr = input().strip().split(' ')
    arrays(arr)


if __name__ == '__main__':
    main()
