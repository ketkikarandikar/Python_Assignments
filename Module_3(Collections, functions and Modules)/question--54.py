# How will you set the starting value in generating random numbers?

# import random module
import random 
for i in range(1):

	# Any number can be used in place of '0'.
	random.seed(0)

	# Generated random number will be between 1 to 1000.
	print(random.randint(1, 1000)) 
	
