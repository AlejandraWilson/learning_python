#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence



length = 30
#print(length)
seq = ''
at = 0.6
count = 0
for i in range(length):
	r = random.random()
	#NOT random.randint because then you'll either get 0 or 1
	if r < 0.6:
		n = random.randint(2,3)
		#if r == 2: print('A', end='')
		if n ==2: seq += 'A'
		#else: print('T', end='')
		else: seq += 'T'
	else:
		n = random.randint(4,5)
		#if r == 4: print('C', end='')
		if n == 4: seq += 'C'
		#else: print('G', end='')
		else: seq += 'G'

print(seq)

for i in seq:
	if i == 'A' or i == 'T':
		count += 1
	#if i == 'T':
		#count += 1
	fraction = float(count/length)
print('%d %.3f %s' % ((len(seq), fraction, seq)))

"""
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
