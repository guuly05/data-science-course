# we import the numpy library to help us with our data analysis
import numpy as np 
# this function helps us with getting data from a file
data = np.genfromtxt('nyc_taxis (1).csv', delimiter = ',', skip_header = True) # delimiter is used to separate the data in the file, skip_header is used to skip the first row of the data since it contains the names of the colomns.
# we need to check the dimension of this function
data.ndim
# we use an attribute that helps us find out the shape of the data 
data.shape
	#(89560 #(this is the number of rides), 15)
# we check the data type of the data 
data.dtype
	# dtype('float64')
# we can also find out more info llike max, min, average etc etc, two colomns from our dataset help us those being 1. trip distance and 2. trip length to find out the speed we use the speed formula distance / time. in order to find those relevent colomns since we left out their names because numpy doesnt accept letters or chars we use slicing.
distance = data[:,7]
# the brackets indicate slicing, 0.[:] means all data in a data set 1.[x,y] x means rows while y means colomns
time = data[:,8]/3600
# colomn 8 is saved as seconds we need to make it into manageable hours in order to do that we divide our results by 3600
speed = distance / time
average_speed = np.mean(speed) 
# this gives us the average speed of all the rides taken using the mean function
print("average speed of thetaxis is: ", average_speed)
	# average speed of the taxis is: 
# in order to lessen these lines of code we can bring them together
speed1 = data[:,7] / (data[:,7])/3600
print("average speed in short form is:", np.mean(speed1))
	# average speeed in short form is: 32.24254....
# next we need to find out how many rides have been taken in the singular month of january. in order to do that we take data from the pickup_month colomn, we need to only extract all the rides ordered in janurary using conditions 
months = data[:,2]
# since we only need january lets extract from the data in month 
january = months ==1 # this is a condition that allows us to save all the months in january in order to find out how many rides have been taken in january we use a function called sum.
print("in the month of january a taxi has been ordered this amount is: ", january.sum())
	# in the month of january a taxi has been ordered this amount is: 13481
# now lets make this shit one line 
jan = data[:,1] == 1
print("this is the improved one line code: ", jan.sum())
	# this is the improved one line code: 13481
# lets find out how much money came from the month of january, in order to do this we use the total_amount generated in the month of january. 
total_amount = data[:,13] 
jan_earning = np.sum(total_amount[jan])
print("the sum of january earnings is: ", jan_earning)
# we can also find the average earnings in january
jan_average = np.mean(total_amount[jan])
print("the average earnings in january is: ", jan_average)
# this var stores for us the tips given in the month of january, we can also find out the average tip in january and the total amount of tips given in january.
tips = data[:,-3]
averaget = np.mean(tips)
averagejan = tips[jan]
print("the average tip in january is: ", np.mean(averagejan) ) # we use np.mean to find the average tip in january
print("total amount of tips is: ", np.sum(averagejan)) # we use np.sum to find the total amount of tips in january
# we try and find more complex conditions like how many tips are above 11 dollars, in order to do that we use a condition that allows us to extract all the tips above 11 dollars.
tips_above_11 = tips[tips > 11]
print("total amount of tips above 11 is: ", np.sum(tips_above_11))