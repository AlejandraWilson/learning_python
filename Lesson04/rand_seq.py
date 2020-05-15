#!/usr/bin/env python3

# Create a program that generates random sequences in FASTA format
# Each name should be unique
# Length should have a minimum and maximum
# GC% should be a parameter
# Use assert() to check bounds of command line values
# When creating sequences, append and join
# Command line:
#	python3 rand_seq.py <# of seqs> <min> <max> <gc>

import random
import sys

number = int(sys.argv[1])
min = int(sys.argv[2])
max = int(sys.argv[3])
gc = float(sys.argv[4])

assert(min>0)
assert(max<1e10)
assert(0<gc<1)
assert(0<number<1e10)

#also want to say "make this number of random sequences"
for i in range(0, number):
	length = random.randint(min, max)
	sequence = []
	for j in range(0, length):
		r = random.random()
		if r < gc:
			r = random.randint(0,1)
			if r == 0:
				sequence.append('G')
			else:
				sequence.append('C')
		else:
			r = random.randint(0,1)
			if r == 0:
				sequence.append('A')
			else:
				sequence.append('T')
	
	print(f'>seq-{1+i}')
	#the f statement lets you know that you'll be printing a thing that's
	#a combination of the set string and also something that changes
	#(the thing in the curly bracket)
	print(''.join(sequence))




"""
python3 rand_seq.py 3 10 20 0.5
>seq-0
GCGCGACCTTAT
>seq-1
ATCCTAGAAGT
>seq-2
CTTCGCTCGTG
"""

