## Day 6 #########################################################################
from pathlib import Path
import numpy as np
from collections import Counter


file = Path('data/AoC-day6.txt')
assert file.is_file()

lines = open(file, 'rt').readlines()

tups = [eval('tuple([{0}])'.format(line)) for line in lines]
min_x = min([t[0] for t in tups])
max_x = max([t[0] for t in tups])
min_y = min([t[1] for t in tups])
max_y = max([t[1] for t in tups])
width = 1 + (max_x - min_x)
height = 1 + (max_y - min_y)

arr = np.zeros([width, height], dtype=int) # initialize with all zeros

def calc_dist(tupl, x, y):
    '''find Manhattan distance between any tuple and another point'''
    return abs(x-tupl[0]) + abs(y-tupl[1])

def find_closest_tupl(tupl_list, x, y):
    '''return the closest tuple(s) to any given point as list'''
    min_dist = min([calc_dist(t,x,y) for t in tupl_list])
    return [1+en[0] for en in enumerate(tupl_list) if calc_dist(en[1],x,y)==min_dist]

def array2list(arr):
    lol = arr.tolist() # produce list of lists
    l = []
    for i in lol:
        l += i # append each sublist to create single list
    return l

def find_border_cases(arr):
    '''if tuple is closest tuple to border point, then its area
       is infinite'''
    s1 = set(arr[0,:]) # top
    s2 = set(arr[:,-1]) # right
    s3 = set(arr[-1,:]) # bottom
    s4 = set(arr[:,0]) # left
    return s1.union(s2).union(s3).union(s4)

for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        best_list = find_closest_tupl(tups, i, j)
        if len(best_list) > 1:
            arr[i-min_x, j-min_y] = 0
        else:
            arr[i-min_x, j-min_y] = best_list[0]


arrlist = array2list(arr)
counts = Counter(arrlist)
border = find_border_cases(arr)

max_size = max([d[1] for d in counts.items() if d[0] not in border])

# part 2
arr2 = np.zeros([width, height], dtype=bool) # initialize with all False

def find_sum_dist(tupl_list, x, y):
    '''return the maximum distance to tuples for each point'''
    return sum([calc_dist(t,x,y) for t in tupl_list])


for i in range(min_x, max_x+1):
    for j in range(min_y, max_y+1):
        arr2[i-min_x, j-min_y] = find_sum_dist(tups, i, j) < 10000

arrlist2 = array2list(arr2)
sum(arrlist2) # total number of points in region
