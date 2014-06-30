import generate_training as images
import initialize_parameters as ip
import numpy as np
visible=8*8 						# number of input units
hidden_size = 25 				# number of hidden units
sparsityParam = .01
lambda_1 = 0.0001;     	# weight decay parameter       
beta = 3;            		# weight of sparsity penalty term       

image = images.load_data()
val = np.array(images.gen_patch(image))
theta = ip.initial(hidden_size,visible)

