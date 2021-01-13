# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# "We can compute the maximum subarray sum ending at position i for all positions i
# by iterating once over the array. As we go, we simply keep track of the maximum sum 
# we've ever seen."

def max_subarray(numbers):
    best_sum = 0  # or: float('-inf')
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum

p = int((input()).split()[1])
profit = list(map(lambda z: int(z) - p, input().split()))
print(max_subarray(profit))