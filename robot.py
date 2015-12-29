import itertools
import operator
import sys
from collections import Counter
from math import factorial

def npermutations(l):
    num = factorial(len(l))
    mults = Counter(l).values()
    den = reduce(operator.mul, (factorial(v) for v in mults), 1)
    return num / den


def passcrack():
	list1=[]
	username=raw_input("username:")
	password=raw_input("password:")
	i=username
	print "\nEnter as much information as possible(as much as a good social engineer might be able to gather).Enter 'end' when done."
	print '\nFor example: Nickname, Birthdate etc.'
	while i!='end':
		list1.append(i)
		i=raw_input()
	list2=[]
	count=0
	
	for i in range(0,len(list1)):
		if list1[i].split(' ') not in list2:
			list2.append(list1[i].split(' '))
			count=count+1
		elif list1[i].split('_') not in list2:
			list2.append(list1[i].split('_'))
			count=count+1	


	final_list=[]
	for i in range(0,len(list2)):
		for j in range(0,len(list2[i])):
			if list2[i][j] not in final_list:
				final_list.append(list2[i][j])
	

	l=len(final_list)
	for i in range(0,l):
		if final_list[i].isupper():
			final_list.append(final_list[i].lower())
		if final_list[i].islower():
			final_list.append(final_list[i].upper())	
		elif final_list[i].istitle():
			final_list.append(final_list[i].lower())
			final_list.append(final_list[i].upper())	

				
	l=len(final_list)		
	for i in range(0,l):
		if final_list[i][0].isupper():
			if final_list[i][0].lower() not in final_list:
				final_list.append(final_list[i][0].lower())
		elif final_list[i][0].islower():
			if final_list[i][0].upper() not in final_list:
				final_list.append(final_list[i][0].upper())


	stuff=final_list	
	count=0
	total=npermutations(stuff)
	for L in range(0, len(stuff)+1):
		for subset in itertools.combinations(stuff, L):
			length_of_subset=len(''.join(subset))

			if length_of_subset<4 or length_of_subset>20:
				count+=npermutations(subset)
				continue
			for permutation_of_combination in itertools.permutations(subset,len(subset)):
				count+=1
				sys.stdout.write("Checking %s :%i of %i    \r" % (''.join(permutation_of_combination),count,total) )
				if ''.join(permutation_of_combination) == password:
					print ("\nThe Force is not strong with this one!")
					exit(0)
	# for L in range(0, len(stuff)+1):
	# 	for subset in itertools.permutations(stuff, L):
	# 		count+=1
	# 		sys.stdout.write("Checking: %i of %i    \r" % (count,total) )
	# 		if ''.join(subset)==password:
	# 			print '\nFOUND!!!. It is a weak password'
	# 			print 'Password is: '+''.join(subset)+'\n'
	# 			return
	# 		sys.stdout.flush()	

passcrack()	    			


