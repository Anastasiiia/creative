# -*- coding: utf-8 -*-
import random


def CheckBox(Box):
	for row in Box:
			if sum(row)!=13: return False
	
	if sum([Box[i][i] for i in xrange(6)])!=13: return False
	if sum([Box[5-i][i] for i in xrange(6)])!=13: return False
	
	
	return True
	gvrt
	
step=0
result=Falseert
while result==False:
	step+=1
	Box=CreatRandomBox()
	result=CheckBox(Box)
	
	if step%10000==0: print step
else:
	print step
	printBox(Box)


