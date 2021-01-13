from sys import stdin

queue = []
stack = []
pri_queue = []

queue_status = True
stack_status = True
pri_queue_status = True

# checks to see if list is empty
# and if the element matches

def removeTup(line, queue_status, stack_status, pri_queue_status):
	tup = line.split()
	if(queue_status == True): 
		if(len(queue) == 0 or queue[0] != str(tup[1])):
			queue_status = False
		else:
			queue.pop(0)
	if(stack_status == True):
		if(len(stack) == 0 or stack[len(stack)-1] != str(tup[1])):
			stack_status = False
		else:
			stack.pop()
	if(pri_queue_status == True):
		if(len(pri_queue) == 0 or pri_queue[len(pri_queue)-1] != int(tup[1])):
			pri_queue_status = False
		else:
			pri_queue.pop()
	return queue_status, stack_status, pri_queue_status

# if input is an integer, it will be assigned to num
# otherwise, it is a line after the integer
# and it will be parsed
# originally started with tuples, but 2 digit numbers made it difficult

for line in stdin:
	try:
		num = int(line)
		queue_status = True
		stack_status = True
		pri_queue_status = True
	except ValueError:
		if (num == 1):
			tup = line.split()
			if(tup[0] == '1'):
				if(queue_status == True and stack_status == False and pri_queue_status == False):
					print("queue")
				elif(queue_status == False and stack_status == True and pri_queue_status == False):
					print("stack")
				elif(queue_status == False and stack_status == False and pri_queue_status == True):
					print("priority queue")
				elif(queue_status == False and stack_status == False and pri_queue_status == False):
					print("impossible")
				else:
					print("not sure")
			if(tup[0] == '2'):
				queue_status, stack_status, pri_queue_status = removeTup(line, queue_status, stack_status, pri_queue_status)
				if(queue_status == True and stack_status == False and pri_queue_status == False):
					print("queue")
				elif(queue_status == False and stack_status == True and pri_queue_status == False):
					print("stack")
				elif(queue_status == False and stack_status == False and pri_queue_status == True):
					print("priority queue")
				elif(queue_status == False and stack_status == False and pri_queue_status == False):
					print("impossible")
				else:
					print("not sure")
			queue = []
			stack = []
			pri_queue = []
			continue
		tup = line.split()
		if(tup[0] == '1'):
			queue.append(tup[1])
			stack.append(tup[1])
			pri_queue.append(int(tup[1]))
			pri_queue.sort(reverse=False)
		elif(tup[0] == '2'):
			tup = line.split()
			queue_status, stack_status, pri_queue_status = removeTup(line, queue_status, stack_status, pri_queue_status)
		num -= 1