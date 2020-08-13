# It's your turn to import and use the math module. Use the math module to calculate e to the 
# power of 3. print the answer.
# print e to the power of 3 using the math module

import math


def e(num):
	power = math.exp(num)
	return power
	

x = e(5)
print(x)