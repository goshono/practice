import random
import statistics

# random.randint(0, 100)

nums = [1, 6, 36, 5, 2, 39, 55, 55]

ave = statistics.mean(nums)
median = statistics.median(nums)
mode = statistics.mode(nums)

print(ave)
print(median)
print(mode)
