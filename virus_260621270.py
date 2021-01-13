# before is the first line
# after is the second line
# The program starts trimming from the front it stops when a char in the first 
# string doesn't correspond with the second string. Then it does the same 
# thing from the reverse and returns the length of the remainder or 
# the virus itself.

before = input()
after = input()

while(len(before)!=0 and len(after)!=0 and before[0] == after[0]):
  before = before[1:]
  after = after[1:]

while(len(before)!=0 and len(after)!=0 and before[-1] == after[-1]):
  before = before[:-1]
  after = after[:-1]

print(len(after))