## Day 2 #########################################################################
from collections import Counter

f = 'data/AoC-day2.txt'
fo = open(f, 'rt')
ids = [i.strip() for i in fo.readlines()]

def test_it(s):
  '''Test string for 2 and 3 of same character'''
  c = Counter(s)
  is_3 = 3 in c.values()
  is_2 = 2 in c.values()
  return [is_2, is_3]

def build_lol(l):
  lol = []
  for i in l:
    lol.append(test_it(i))
  return lol

lol = build_lol(ids)
twos = sum([i[0] for i in lol])
threes = sum([i[1] for i in lol])
checksum = twos * threes

# part 2
def find_diff(s1, s2):
  c = 0
  for i in range(len(s1)):
    c += int(s1[i] != s2[i])
  return c

def produce_similar(sl):
  sims = ''
  for i in range(0,len(sl[0])):
    if sl[0][i] == sl[1][i]:
      sims += sl[0][i]
  return sims

similar_list = []
for i in range(0, len(ids)-1):
  for j in range(i, len(ids)):
    if find_diff(ids[i], ids[j]) == 1:
      similar_list.append([ids[i], ids[j]])

for pair in similar_list:
  print(produce_similar(pair))