# split takes the list of numbers and the 2nd input, the width
# the program proceeds to take the difference between every single element
# and every other element. the result will then have the 0 removed,
# sorted and printed

def split(numbers, w):
	s = len(numbers)
	numbers.append(0)
	numbers.append(w)
	numbers = sorted(numbers)
	lower = 0
	mylist =[]
	for x in numbers:
		for y in numbers:
			mylist.append(abs(y-x))
	mylist = list(dict.fromkeys(mylist))
	mylist.remove(0)
	return sorted(mylist)

variables = input().split()
w = int(variables[0])
num_line = input().split()
print(*split(list(map(int, num_line)), w), sep = ' ')