#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# Use fileinput to get the data from nucleotides.txt
# Make sure that the values are probabilities
# Make sure that the distribution sums to 1
# Report with 3 decimal figures

import fileinput
import math

data = []
for line in fileinput.input():
	#if line[0] == '#': continue # skip over comments
	if line.startswith('#'): continue # same as above
	line = line.rstrip() # remove newline (return character), often useful
	ln = line.split()
	#split divides each line into a list, separated by spaces
	data.append(float(ln[1])) # store the data
	#ln[1] is the second item in this 'list' (the list starts with 0)

#you just want to retrieve the nucleotide frequencies from the file
#you don't even care which frequences are attached to which nucleotide
#you'll do a "for" loop, and a "+=" since you're summing the things up
#you'll have also designated a variable called 'H'

H = 0
for i in data:
	H -= i * math.log(i, 2)
print('{:.3f}'.format(H))
#('.3f%' % (H))



"""
python3 entropy.py nucleotides.txt
1.846
"""
