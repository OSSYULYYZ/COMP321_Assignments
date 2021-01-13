# There was not enough time during the competition to code this!
# I was a COMP322(C++) TA in 2019-01 after taking the course in the previous year.
# That is how I know how to read C++. I checked my answer with the following
# URLs:

# https://github.com/kantuni/Kattis/blob/master/kleptography.cpp
# https://github.com/iandioch/solutions/blob/master/kattis/kleptography/solution.py

n, m = map(int, input().split())
key = input()
text = input()

output = list(' '*(m - n) + key)
for i in range(m - 1, n - 1, -1):
  output[i - n] = chr(ord('a') + (ord(text[i]) - ord(output[i])) % 26)
print(''.join(output))