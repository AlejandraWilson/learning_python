#!/usr/bin/env python3

import gzip
import sys
import math
import random

# Write a program that creates random fasta files
# Create a function that makes random DNA sequences
# Parameters include length and frequencies for A, C, G, T
# Command line: python3 rand_fasta.py <count> <min> <max> <a> <c> <g> <t>

program = sys.argv[0]
#just stating this for my benefit
count = int(sys.argv[1])
#number of FASTA files to create
min = int(sys.argv[2])
#minimum length of the FASTA sequence allowed
max = int(sys.argv[3])

afreq = float(sys.argv[4])
#frequence of nucleotide 'A'
cfreq = float(sys.argv[5])
gfreq = float(sys.argv[6])
tfreq = float(sys.argv[7])
assert afreq + cfreq + gfreq + tfreq == 1

#print(count, min, max, afreq, cfreq, gfreq, tfreq)

def makeseq():
#this function will make random DNA sequences
	for j in range(count):
#you'll make a DNA sequence for each number in 'count'
		sequence = []
#have to create your empty list first before you can do stuff with it
		length = random.randint(min, max)
#establishes the minimum and maximum possible lengths of your string
		for n in range(length):
			r = random.random()
			if r < afreq:
				sequence.append('A')
			elif r < (afreq + cfreq):
				sequence.append('C')
			elif r < (afreq + cfreq + gfreq):
				sequence.append('G')
			else:
				sequence.append('T')
		sequence = ''.join(sequence)
#if you didn't join it it'd look like ['A'] ['G'] ['T'] etc.
		print(f'<seq{j}> {sequence}')
#gives you a nice little label for each sequence
	return makeseq
#let's the function know that it's 'done'
	
makeseq()
#'calls' the function, i.e. tells the program to actually do the function now


	




"""

"""
