## Day 5 #########################################################################
from pathlib import Path
import re

def shorten(string):
    new = string
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        new = re.sub('{0}{1}'.format(letter, letter.upper()), '', new)
        new = re.sub('{0}{1}'.format(letter.upper(), letter), '', new)
    return new

def loop_shorten(string):
    old = string
    new = shorten(string)
    while old != new:
        old = new
        new = shorten(new)
    return new

file = Path('data/AoC-day5.txt')
assert file.is_file()
with open(file, 'rt') as fo:
    full = fo.read()

short = loop_shorten(full)
len(short)

# part 2
shortest_length = 99999
for letter in 'abcdefghijklmnopqrstuvwxyz':
    test = re.sub(letter,'',full)
    test = re.sub(letter.upper(),'',test)
    short = loop_shorten(test)
    if len(short) < shortest_length:
        best_letter = letter
        shortest_length = len(short)

shortest_length, best_letter