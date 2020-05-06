#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

w = 3
#print(dna)
for i in range(len(dna)-w+1):
	codon = dna[i:i+w]
	if (i+3) %3 == 0:
		print(codon)
		

"""
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
