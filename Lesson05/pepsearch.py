#!/usr/bin/env python3

import gzip
import sys

# Write a program that finds peptidies within protein sequences
# Command line:
#	python3 pepsearch.py IAN


def read_fasta(filename):
	name = None
	seqs = []
	
	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()
#All this does . . . something

file = sys.argv[1]
peptide = sys.argv[2]
for name, seq in read_fasta(file):
	if peptide in seq:
		print('found', name)
#looks at all the FASTA files
#gives you the name of the sequence (ex: Clp)
#and the number of amino acids (ex: 420)
#also defines what the stuff you put into the command line will mean
#lets you look for specific peptide strings (ex: BOII) in each FASTA file
#tells you if the file contains that peptide
longest = None
shortest = None
for name, seq in read_fasta(sys.argv[1]):
	break
	if len(seq) > longest: longest = len(seq)
	if len(seq) < shortest: shortest = len(seq)
print(shortest, longest)
#gives you the longest and shortest FASTA files



"""
python3 pepsearch.py proteins.fasta.gz IAN | wc -w
	43
"""
