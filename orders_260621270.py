# Coin Change as a 2D DP
# https://www.geeksforgeeks.org/coin-change-dp-7/
# COMP321-Lecture5-DP Solution Idea #1:
def count(S, m, n):
  if (n == 0):
    return 1
  if (n < 0): 
    return 0 
  if (m <=0 and n >= 1):
    return 0
  return count(S, m - 1, n) + count(S, m, n - S[m - 1])

# Top-Down DP
# COMP321-Lecture5-DP Solution Idea #2:
table = [0]
def topDownDP(numItems, itemCosts, numOrders, orderPrices):
  for i in range(max(orderPrices) + max(itemCosts)):
    table.append(-1)
  for i in range(numItems):
    for j in range(max(orderPrices) + 1):
      if table[j] == -2:
        table[j + itemCosts[i]] = -2
      if table[j] >= 0:
        if table[j + itemCosts[i]] == -1:
          table[j + itemCosts[i]] = i
        else:
          table[j + itemCosts[i]] = -2

numItems = int(input())
itemCosts = list(map(int, input().split(" ")))
numOrders = int(input())
orderPrices = list(map(int, input().split(" ")))

topDownDP(numItems, itemCosts, numOrders, orderPrices)

for total in orderPrices:
  if(table[total] == -1):
    print("Impossible")
  elif(table[total] == -2):
    print("Ambiguous")
  else:
    order = []
    while total > 0:
      order.append(table[total] + 1)
      total = total - itemCosts[table[total]]
    if total < 0:
      print("Ambiguous")
    else:
      print(*sorted(order), sep = ' ')