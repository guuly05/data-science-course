# first we import NumPy

import numpy as np 

# how do we create an array using np

p = np.array([48.858598, 2.294495]) # creating array from list
p.ndim # getting dimension of array P
p.shape # getting the is of each array dimension
len(p) # getting dimension length of array P
p.dtype # getting data type of array P 

# you can create an empty array from scratch without initializing any elements on it 
np.empty([3,2], dtype=np.float64)
	# array([[0,0], [0,0], [0,0]])
a = np.array([[1,2], [3,4]])
np.empty_like(a) # free up memory locations of any given array 
	# array([[0,0], [0,0], [0,0]])

# you can create a array with default value of one
np.ones(5)
	# array([1,1,1,1,1])
x = np.array([[0,1,2], [3,4,5]])

# you can also create an array with even spaced values in a given interval
np.arange(2,5)
# array([2,3,4])
np.arange(4, 12, 5) # we tell it to find us numbers between 4 and 12 and a gap of 5 between them hence why we get [4, 9] 
	# array([4, 9])

# now that you masted how to create an array we will apply some mathematical operations to array data without writing any loops

cali = np.ones(4)
cali*2 
	# array([2,2,2,2]) 

fahad = np.ones(4)
	# array([1,1,1,1])
fahad + 3
	# array([4,4,4,4])

nimco = np.shape([[0,5,10], [20,25,30]])
nimco.reshape(3,2) # this method helps us reshape an array into however we want by changing the structure (true black pill)
	# array([[0,5],[10, 20],[25,30]])
nimco.T # transpose basically replaces them in reletive to their colomn
	# array([[0,20],[5, 25],[10,30]])

# numpy has round up, down floor ceeling etc etc 
sagal = np.shape([0.5, 33.6])
sagal.roundup

# numpy also has elemntwise comparison 
safa = [0,1,4]
yaxye = [10,20,30]
np.greater(safa, yaxye) # the output will always be boolean
	# array([[false, false, false], [false, false, false]], dtype=bool)

# you can also calculate all the elmeents along any given axis
aldidi = np.array([[2,4], [3,5]])
aldidi.sum(a, axis=0)
	# array([6,20])

# you can also calculate standard deviation and variance 
dxya = np.array([[2,4], [3,5]])
dxya.std(a)
	# 1.1180339
dxya.var(a)
	# 1.15

# how do we save our results in a file

jouske = np.array([[2,4], [3,5]])
np.save('test1.npy', jouske)

# we can load/read from a numpy/text file

np.load('test1.npy')
	# array(([[2,4], [3,5]]))