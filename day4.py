## Day 4 #########################################################################
from pathlib import Path
from collections import Counter
import re

file = Path('data/AoC-day4.txt')
assert file.is_file()
fo = open(file, 'rt')
raw = sorted([x.strip() for x in fo.readlines()]) # will sort by timestamp

minutes = []
guard = []
status = []
for line in raw:
  minutes.append(int(re.findall(':\d\d', line)[0].split(':')[1]))
  status.append('Asleep' if re.findall('asleep', line) != [] else 'Awake')
  try:
    guard.append(int(re.findall('Guard #\d+', line)[0].split('#')[1]))
  except:
    guard.append(None)

for i in range(len(guard)):
  if guard[i] == None:
    guard[i] = guard[i-1]

assert len(minutes) == len(guard)
merged = zip(guard, minutes, status)

all = []
for g in merged:
    if g[2] == 'Asleep': # is sleep event
        g1 = next(merged) # next event (not asleep)
        ms = range(g[1], g1[1]) # minutes asleep
        for m in ms:
            all.append((g[0], m))

guard_all = [i[0] for i in all]
guard_count = Counter(guard_all)
best_guard = [i for i in guard_count
                if guard_count[i] == max(guard_count.values())][0]

minute_potentials = [i[1] for i in all if i[0] == best_guard]
minute_count = Counter(minute_potentials)
best_minute = [i for i in minute_count
                if minute_count[i] == max(minute_count.values())][0]

solution = best_guard * best_minute

# part 2
c = Counter(all)
best_minute = [(i, c[i]) for i in c if c[i] == max(c.values())][0]
solution = best_minute[0][0] * best_minute[0][1]