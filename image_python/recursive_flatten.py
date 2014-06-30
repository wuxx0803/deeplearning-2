x=[1,2,3,[6,3,4]]

def flatten(lst,acc):
	t=lst.pop()	
	h=lst 
	if type(t) == type([]):
		flatten(t,acc)
	else:
		acc.append(t)
		flatten(h,acc)

acc=[]
flatten([1,2,[3,4]],acc)
print acc
