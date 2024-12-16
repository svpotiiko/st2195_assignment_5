# intitial code
def is_divisible_by_k(x, k):
# Checks whether x is divisible by k.

# change : added returning variable
	result = 0
	if (x % k) == 0:
		result = 1
	return result
	
# Store all the integers that are multiples of 2 or 5 or 7 that are lower
# or equal to 1000 (excluding doubles)

# change : increased range in for loop to make variables are lower or 
# equal t0 1000
# change : switched initial if statement to OR instead of AND
# chnage : divisivble by 2,5,7,  not 2,3,7
# change : x to i in if statement
# change : x into list instead of tuple to use append

x = []
for i in range(1001):
	if (is_divisible_by_k(i, 2) == 1 or is_divisible_by_k(i, 5)) == 1 or is_divisible_by_k(i, 7) == 1: 
		x.append(i)

# Sum all the integers that are multiples of 2 or 5 or 7 that are lower
#or equal to 1000 (excluding doubles)

answer = sum(x)
print(answer)