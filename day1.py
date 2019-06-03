## Day 1 #########################################################################

from pathlib import Path
file = Path('data/AoC-day1.txt')
assert file.is_file()
fo = open(file)
nums = [int(i) for i in fo.readlines()]
sum(nums) #423

# part 2
def loop_nums(l):
  '''Generator to loop through list indefinite number of times'''
  max_i = len(l) - 1
  i = 0
  while True:
    yield(l[i])
    if i < max_i:
      i += 1
    else:
      i = 0

def loop_til_dupe(l):
  '''Find first number that is duplicated'''
  num_iter = loop_nums(l)
  f1 = [0]
  while True:
    f1.append(f1[-1]+next(num_iter))
    if len(set(f1)) < len(f1):
      print("Solution is {}".format(f1[-1]))
      print("Only took {} tries!".format(len(f1)))
      break

loop_til_dupe(nums) # 61126