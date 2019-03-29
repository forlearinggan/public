#!/usr/bin/python3
#!coding=utf-8

import operator
def stack_sort(target,*,key=True):
	if key:
		op=operator.gt
	else:
		op=operator.lt
	assist = []*len(target)
	while target:
		top = target.pop()
		while assist and op(top,assist[-1]):
			target.append(assist.pop())
		assist.append(top)
	while assist:
		target.append(assist.pop())

if __name__ == '__main__':
	stack = [3,2,4,1,2,4,7,9]
	stack_sort(stack,key=False)
	print(stack)
