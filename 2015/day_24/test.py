from itertools import combinations as combos

nums = sorted([1,2,3,4,5,7,8,9,10,11], reverse=True)
x = sum(nums)//3

#res = [seq for i in range(len(nums), 0, -1)
 #      for seq in combos(nums, i) if sum(seq)
  #     == x]


a = []
b = []
c = [
