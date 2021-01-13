# I have anxiety which causes me to focus on one particular solution.
# It was working for the given input, so I needed some new inspiration:
# https://github.com/cliodhnaharrison/kattis/blob/master/busnumbers.py

n = int(input().strip())
buses = sorted(map(int, input().split()))

buses.append(1002) # max = 1'000 
chain = 1
before = buses[0]
output = []
i = 1
while(i < len(buses)):
  num = int(buses[i])
  if(num == (before + 1)):
    chain += 1
  else:
    if(chain >= 3):
      output.append(str(buses[i - chain]) + "-" + str(buses[i - 1]))
    elif(chain == 2):
      output.append(buses[i - 2])
      output.append(buses[i - 1])
    else:
      output.append(buses[i - 1])
    chain = 1
  before = num
  i += 1
print(*output)