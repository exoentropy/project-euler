import sys

MAX_NUMBER = 50000
MAX_FIBONACCI = 4000000
#assert: no Fibonacci number can equal -1
cache = [-1] * MAX_NUMBER
#set initial values
cache[1] = 1
cache[2] = 2
#account for first even Fibonacci number (2)
sumOfEvens = 2

for number in range(3, MAX_NUMBER):
	cache[number] =  cache[number - 2] + cache[number - 1]
	if (cache[number] > MAX_FIBONACCI):
		break
	if (cache[number] % 2 == 0):
		sumOfEvens += cache[number]

print sumOfEvens