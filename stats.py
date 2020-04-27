#!/usr/bin/env python3

from math import sqrt
import fileinput

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import any other modules!

numbers = []
for line in fileinput.input():
	if line.startswith('#'): continue
	line = line.rstrip()
	numbers.append(float(line))
import sys
assert(len(sys.argv) == 2)
program = sys.argv[0]
file = sys.argv[1]
assert(program == 'stats.py')
#do the calculations for things, and then the assertions
numbers.sort()
total = 0
for n in numbers:
	total += n

count = len(numbers)
mean = total/count
addup = 0
for n in numbers:
	addup += ((n - mean)**2)
stdev = sqrt(addup/count)

oddmedian = numbers[int((len(numbers)/2))]
lowmedian = numbers[(int((len(numbers)/2))-1)]
highmedian = numbers[(int((len(numbers)/2)))]

min = numbers[0]
max = numbers[count-1]
print('Count:', count)
print('Min:', min)
print('Max:', max)
print('Mean:', mean)
print('Stdev:', '%.3f' % (stdev))
if count%2 == 1:
	print('Median:',oddmedian)
else: print('Median:',((lowmedian + highmedian)/2))

assert(max >= 0)
assert(mean > 0)
assert(stdev > 0)






"""
python3 stats.py numbers.txt
Count: 10
Minimum: -1.0
Maximum: 256.0
Mean: 29.147789999999997
Std. dev: 75.777
Median 2.35914
"""
