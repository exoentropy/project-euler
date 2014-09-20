import sys

MAX = 1000
sumOfMultiples = 0

for number in range(1, MAX):
	if (number % 3 == 0) | (number % 5 == 0):
		sumOfMultiples += number

print sumOfMultiples