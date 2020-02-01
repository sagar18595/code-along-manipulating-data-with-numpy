# --------------
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import sys
import csv

# Command to display all the columns of a numpy array
np.set_printoptions(threshold=sys.maxsize)
# Load the data. Data is already given to you in variable `path` 
data = np.genfromtxt(path,dtype = str,delimiter = ",",skip_header = 1)

#print (data)

# How many unique ad campaigns (xyz_campaign_id) does this data contain ? And for how many times was each campaign run ?
from collections import Counter

print (Counter(data[:,1]))

# What are the age groups that were targeted through these ad campaigns?
print (np.unique(data[:,3]))
# What was the average, minimum and maximum amount spent on the ads?
average = data[:,-3].astype(float).mean()
minimum = data[:,-3].astype(float).min()
maximum = data[:,-3].astype(float).max()

print (average,minimum,maximum)

# What is the id of the ad having the maximum number of clicks ?

id_max_click= data[data[:,-4].astype(np.int64) == data[:,-4].astype(np.int64).max()][:,0].astype(int)
print(id_max_click)

# How many people bought the product after seeing the ad with most clicks? Is that the maximum number of purchases in this dataset?

print (data[data[:,0].astype(np.int64) == id_max_click][:,-1].astype(np.int64))
 
# So the ad with the most clicks didn't fetch the maximum number of purchases. Let's find the details of the product having maximum number of purchases

print (data[data[:,-1].astype(np.int64) == data[:,-1].astype(np.int64).max()])

# Create a new feature `Click Through Rate`  (CTR) and then concatenate it to the original numpy array 

CTR = np.array(np.divide(data[:,-4].astype(np.int64),data[:,-5].astype(np.int64))*100)

# Create a new column that represents Cost Per Mille (CPM) 

CPM = np.array(np.divide(data[:,-3].astype(float),data[:,-5].astype(float))*100)

print (data.shape, CTR.reshape(-1,1).shape, CPM.reshape(-1,1).shape)
data = np.concatenate((data,CTR.reshape(-1,1),CPM.reshape(-1,1)),axis = 1)


