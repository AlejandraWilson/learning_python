#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

sequence = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
#w = 11

#experiment: writing it as a function now
def gc(seq):

	for nt in seq:
		count = 0
		if nt == 'G' or nt == 'C':
			count +=1
		return count/(len(seq))

for i in range(0, len(sequence)-w+1):
	print(i, seq[i:i+w], gc(seq[i:i+w]))
	#seq = sequence[i:i+w]
	#defining the size of the window for the program

	#print(i, s, gc(s,)








"""
gc = 0
#need to start the gc percentage off at zero to give you a place to start

for i in range(0, len(seq)-w+1):
#i denotes a number
	count = 0
#need the count to start over at 0 for each window (otherise it'll keep adding up)
	kmer = seq[i:i+w]
#defining the size of the kmer
	for nt in kmer:
#nt denotes a character in the string
		if nt == 'G' or nt == 'C': count +=1
	gc = count/w
#calculates the gc fraction in a window of size w
	print('%d %s %.4f' % (i, kmer, gc))
#gets the printed answer looking pretty



0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
