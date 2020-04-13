#!/usr/bin/env python3

# Print out all the codons for the sequence below in reading frame 1
# Use a 'for' loop

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

k = 3
for i in range(0, len(dna), -k+1):
	kmer = dna[i:i+k]
	print(kmer)



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
