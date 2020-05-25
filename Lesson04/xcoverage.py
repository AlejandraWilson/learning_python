#!/usr/bin/env python3

# Write a program that simulates random BAC coverage over a genome
# Command line arguments include
# 	Genome size (e.g. 1000)
# 	X coverage (e.g. 5)
# Use assert() to check parameter bounds
# Report min, max, and histogram of coverage
# Note that your output may vary due to random function

#this might be similar to the birthday problem
#for a genome of length l, bac length is a window of length w that will
#fall at some random point in range(0,l)
#if a character in "genome" is "hit" by bac, the program should report that
#the default for each character in "genome" is 0, which increases
#by 1 every time a bac covers it
#you'll need to import sys so you can plug stuff into the command line
#you also need to generate a random genome of length l

import sys
import random
program = sys.argv[0]
#referring here to xcoverage; line 22 isn't strictly necessary but helps me
size = int(sys.argv[1])
coverage = float(sys.argv[2])
assert(size > 1)
assert(coverage > 0)
assert(len(sys.argv) == 3)

genome = [0] * size
#the number of bacs you need to have an average coverage of x is
#genome size * x
bacs = int(size * coverage)
#this says how many bacs I will use
for i in range(bacs):
	r = random.randint(0, size-1)
	genome[r] +=1

genome.sort()
#print(genome)
min = genome[0]
max = genome[-1]
print(f'Size: {size}')
print(f'X: {coverage}')
print(f'BACs: {bacs}')
print(f'Min: {min}')
print(f'Max: {max}')
counts = [0] * (max+1)
#because the count starts at zero
#this helps count be the same length as genome
mean = 0

for c in genome:
	counts[c] += 1
	mean += c
print(f'Mean: {mean/size}')
print('Counts:')
for i in range(len(counts)):
	print(i, counts[i])



"""
#nt indicates a number (the position in the list 'genome'
#genome[nt] indicates the character at that position
#now make a bac that covers a window of a specified size
#try out a randome number for w and sub it in with the correct number in a bit
	w = 3
	r = random.randint(size+1-w)
	bac = genome[nt+r:nt+r+w]
#now I want to record it when 'bac' hits a spot in 'genome'
#it'll do that by raising genome[nt] by one each time there's a 'hit'
#then I want to report if there are any genome[nt]'s that are zero
#if so
	print(bac)
	
print(genome)



"""
"""
Size: 1000
X: 5.0
BACs: 5000
Min: 0
Max: 13
Counts:
0 5
1 39
2 88
3 144
4 175
5 150
6 151
7 116
8 59
9 40
10 20
11 5
12 6
13 2
"""
