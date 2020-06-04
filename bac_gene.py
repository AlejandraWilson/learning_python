#!/usr/bin/env python3

# Develop a program that finds all the genes in a bacterial genome.
# Program reads FASTA file of genome sequence
# Genes begin with ATG and end with stop codon
# Genes are at least X amino acids long (default 100)
# Genes may be on either strand
# Genes must be given unique names
# Genes must be reported in a FASTA file as their protein sequence
# Also create a genome report containing the following information
	# Size of the genome in bp
	# Number of genes
	# Percentage of genome that is coding
	# Number of genes on the positive strand
	# Number of genes on the negative strand

import random
import argparse
import biotools as bt

parser = argparse.ArgumentParser(
	description='Prokaryotic gene finder.')
parser.add_argument('--file', required=True, type=str,
	metavar='<str>', help='FASTA file')
parser.add_argument('--minorf', required=False, type=int, default=300,
	metavar='<int>', help='minimum open reading frame length [%(default)i]')

arg = parser.parse_args()

gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

def anti(seq):
	forward = 'ACGTRYMKWSBDHV'
	reverse = 'TGCAYRKMWSVHBD'
	table = seq.maketrans(forward, reverse)
	return seq.translate(table)[::-1]
	#defines the reverse sequence

def get_orfs(seq, min):
	orfs = []
	stop_used = {}
	for i in range(len(seq) - 2):
		codon = seq[i:i+3]
		if codon == 'ATG': 
			atg = i
			for j in range(atg + 3, len(seq) - 2, 3):
				codon = seq[j:j+3]
				if codon == 'TAG' or codon == 'TAA' or codon == 'TGA':
					break
			stp = j + 2
			if stp - atg + 1 > min and stp not in stop_used: 
				stop_used[stp] = True
				orfs.append(seq[atg:stp +1])	
	return orfs
	#looks at genome and creates list of all the orfs, once it finds stop codon it ends orf
	#and begins new orf at next start codon

def translate(orf):
	pro = []
	for i in range(0, len(orf), 3):
		codon = orf[i:i+3]
		if codon in gcode: pro.append(gcode[codon])
		else:              pro.append('X') 
	return ''.join(pro)
	#looks at each orf and translates it into amino acids

def comp(seq):
	A = seq.count('A')
	C = seq.count('C')
	G = seq.count('G')
	T = seq.count('T')
	total = A + C + G + T
	return A/total, C/total, G/total, T/total
	#tells us what nt frequency is in actual genome
	
def randseq(length, a, c, g, t):
	pool = int(a * 100) * "A" + int(c * 100) * "C" + int(g * 100) * "G" + int(t * 100) * "T" 
	seq = []
	for i in range(length):
		seq.append(random.choice(pool))
	return ''.join(seq)
	#uses nt frequency to make random genome

n = 0
len_orfs = 0	
for name, seq in bt.read_fasta(arg.file):
	orfs1 = get_orfs(seq, arg.minorf)
	orfs2 = get_orfs(anti(seq), arg.minorf)
	for orf in orfs1:
		n += 1
		len_orfs += len(orf)
		print(f'>Protein+{n}')
		print(translate(orf))
	for orf in orfs2:
		n += 1
		len_orfs += len(orf)
		print(f'>Protein-{n}')
		print(translate(orf))
	print(f'Number of + genes: {len(orfs1)}')
	print(f'Number of - genes: {len(orfs2)}')
	print(f'Number of genes: {len(orfs1 + orfs2)}')
	print(f'Genome size: {len(seq)}')
	print(f'Coding nts: {len_orfs}')
	print(f'Percentage genome coding: {len_orfs/len(seq)}')

	
	a, c, g, t = comp(seq)
	#count of real genome
	seq = randseq(int(10000), a, c, g, t)
	count = 0
	for orf in get_orfs(seq, arg.minorf):
		count += 1
	for orf in get_orfs(anti(seq), arg.minorf):
		count += 1
	#counts/prints how many orfs are in the random sequence
	print(f'A: {a}, C: {c}, G: {g}, T: {t}')
	print(f'Random orfs: {count}')

add_bp = 0
for bp in seq:
	add_bp += 1
print(f'Rand_genome size: {add_bp}')


"""
Size of the genome in bp
Number of genes
Percentage of genome that is coding
Number of genes on the positive strand
Number of genes on the negative strand
"""








