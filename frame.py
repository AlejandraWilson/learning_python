#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

k = 1
for i in range(0, len(dna), k):
#This makes it so the program is giving a result
#for each letter individually across this string of letters
		
	kmer = dna[i]
	print(i, i%3, kmer)


"""
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
