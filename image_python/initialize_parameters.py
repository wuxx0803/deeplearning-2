import random
import math
import numpy as np

def flatten(*args):
	f =np.hstack([a.flatten() for a in args])
	return f

def initial(hidden_size,visible_size):
###
	r = math.sqrt(6)/math.sqrt(hidden_size+visible_size+1); 
	W1 =  np.random.rand(hidden_size, visible_size)* 2 * r - r;
	W2 =  np.random.rand(visible_size, hidden_size)* 2 * r - r;
	b1 = np.zeros(hidden_size)
	b2 = np.zeros(visible_size)
	return flatten(W1,W2,b1,b2)

#initial(25,64)
