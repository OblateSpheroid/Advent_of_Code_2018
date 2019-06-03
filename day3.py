## Day 3 #########################################################################
from collections import Counter

f = 'data/AoC-day3.txt'
fo = open(f, 'rt')
raw = [i.strip() for i in fo.readlines()]

def parse_it(raw_input):
  '''For given row of input, parse into dictionary'''
  id = raw_input.split('@')[0].strip()
  raw2 = raw_input.split('@')[1].strip()
  from_left = int(raw2.split(',')[0].strip())
  raw3 = raw2.split(',')[1].strip()
  from_top = int(raw3.split(':')[0].strip())
  raw4 = raw3.split(':')[1].strip()
  width = int(raw4.split('x')[0].strip())
  height = int(raw4.split('x')[1].strip())
  return {'id': id, 'from_left': from_left, 'from_top': from_top,
          'width': width, 'height': height}

def which_squares(d):
  '''From a given dictionary (single row of input),
  find which squares belong to that claim'''
  x_start = d['from_left'] + 1
  x_end = d['from_left'] + d['width']
  y_start = d['from_top'] + 1
  y_end = d['from_top'] + d['height']
  los = [] # list of squares for this id
  for i in range(x_start, x_end+1):
    for j in range(y_start, y_end+1):
      los.append((i, j))
  return los

lot = [] # list of tuples
for i in raw:
  l1 = which_squares(parse_it(i))
  for j in l1: lot.append(j) # append element-wise, not list of lists

counts = Counter(lot)
sum([x>1 for x in counts.values()]) # count total with more than one claim

# part 2
def check_id(raw_input):
  '''see if an ID has only single-claim squares'''
  parsed = parse_it(raw_input)
  los = which_squares(parsed)
  for i in range(len(los)):
    this_count = counts[los[i][1:]]
    if this_count > 1:
      return False
      break
  return parsed['id']

for line in raw:
  if check_id(line):
    print(check_id(line))
