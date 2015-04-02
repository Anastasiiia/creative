# -*- coding: utf-8 -*-
import random


def CheckBox(Box):
	for row in Box:
			if sum(row)!=13: return False
	
	if sum([Box[i][i] for i in xrange(6)])!=13: return False
	if sum([Box[5-i][i] for i in xrange(6)])!=13: return False
	
	for i in [0, 2, 4]:
		for j in xrange(6):
			for k in [0, 2, 4]:
				for l in xrange(6):
					if (Box[i][j]==Box[k][l] and Box[i+1][j]==Box[k+1][l]) or (Box[i][j]==Box[k+1][l] and Box[i+1][j]==Box[k][l]):
						return False
	return True
	
	
step=0
result=False
while result==False:
	step+=1
	Box=CreatRandomBox()
	result=CheckBox(Box)
	
	if step%10000==0: print step
else:
	print step
	printBox(Box)


