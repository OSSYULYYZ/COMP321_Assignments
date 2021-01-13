cupOrder = input()

cups = [1,0,0]

# switches order based on cupOrder.

for order in cupOrder:
	if order == 'A': cups[0], cups[1] = cups[1], cups[0]
	if order == 'B': cups[1], cups[2] = cups[2], cups[1]
	if order == 'C': cups[0], cups[2] = cups[2], cups[0]

print((cups.index(1) + 1))