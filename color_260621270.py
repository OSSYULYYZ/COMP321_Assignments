# split takes the list of numbers and the 2nd and 3rd inputs
# the first while loop acts as a for loop for arrays as python only has
# for each loops. then because the list gets sorted, one can start at
# the very end and compare that to the max going down

def split(numbers, c, k):
	s = len(numbers)
	washes = 0
	load = 1
	lower = 0
	numbers = sorted(numbers)

	if(c >= s): return 1
	while lower < len(numbers):
		upper = lower + c - 1
		if upper >= s: upper = s - 1
		for x in numbers:
			if numbers[upper] - numbers[lower] <= k:
				washes += 1
				lower = upper + 1
				break
			upper -= 1
	return washes

variables = input().split()
c = int(variables[1])
k = int(variables[2])
sock_diff = input().split()
print(split(list(map(int, sock_diff)), c, k))