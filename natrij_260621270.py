from datetime import datetime, timedelta

# There was an Run Time Error from the call below:
# tdelta = timedelta(days=0, seconds=tdelta.seconds)
# I ended up correcting that with help from:
# https://github.com/rvrheenen/OpenKattis/blob/master/Python/natrij/natrij.py
# I have anxiety which causes me to focus on one particular solution.
# I did NOT think about the Run Time Error.

FMT = '%H:%M:%S'
t1 = datetime.strptime(input().strip(), FMT)
t2 = datetime.strptime(input().strip(), FMT)

if (t1 == t2):
  print('24:00:00')
else:
  if t1 > t2:
    t2 += timedelta(days=1)
  t3 = t2 - t1
  print("0" + str(t3) if str(t3)[1] == ":" else str(t3))