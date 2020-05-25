#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it
# We will have a variable number of bins (can be months or days)
# And some number of trials for the simulation
# And some number of people whose have random birthdays
# Use assert() to check parameters
# On the command line:
#	python3 birthday.py <bins> <trials> <people>

import random
import sys
#command line: python3 birthday.py #bins #trials #people
file = sys.argv[0]
bins = int(sys.argv[1])
trials = int(sys.argv[2])
people = int(sys.argv[3])

#count up the number of birthdays each day has, and record if the number rises
#for each person, that person is assigned a random number (i.e. birthday)
#in the range(bins)

success = 0
for t in range(trials):

	birthdays = []
	for i in range(bins):
		birthdays.append(0)
	for p in range(people):
	#p denotes a spot in that string of people
	#assign a random number in "bins" (i.e. a birthday) for each person
		b = random.randint(0, bins-1)
		birthdays[b] += 1
	#print(birthdays)

	collisions = False
	for n in birthdays:
		if n > 1:
			collisions = True
			break
	if collisions:
		success += 1
print(success/trials)
		
	






"""
python3 birthday.py 365 1000 23
0.520
"""

