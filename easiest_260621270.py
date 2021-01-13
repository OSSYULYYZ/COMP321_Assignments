num = int(input())

# getting sum of digits
# add the mod of ten gets you the last digit
# return 

def sum_digits(num):
	sum = 0
	while num > 0:
		rem = (num % 10)
		num = num // 10
		sum = int(sum) + rem
	return sum

while num != 0:
	sum_num = sum_digits(num)
	sum_product = 0
	p = 10
	while sum_product != sum_num:
		p += 1
		product = num * p
		sum_product = sum_digits(product)
	print(p)
	num = int(input())