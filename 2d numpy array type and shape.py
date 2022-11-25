baseball=[[180,170],
[120,100],
[140,200],
[120,130],
[134,133],
]
import numpy as mahnoor
mahnoor_baseball=mahnoor.array(baseball)
print(mahnoor_baseball.shape)
print(type(mahnoor_baseball))
#print secod row of the mahnoor_baseball
print(mahnoor_baseball[1,:])
#select entire first column of mahnoor_baseball and store in base variable
base=mahnoor_baseball[:,0]
print(base)
#print eight if 3rd player
print(mahnoor_baseball[2,0])
#mathematical operations on numpy arrays
conversion=mahnoor.array([2,5])
print(mahnoor_baseball+conversion)
print( mahnoor_baseball*conversion)
#selecting first clumn of the list
mahnoor_base=mahnoor.array(mahnoor_baseball[:,0])
#taking mean of the data
print(mahnoor.mean(mahnoor_base))
#taking median of the data()
print(mahnoor.median(mahnoor_base))
#print mean height of first column
#print(mahnoor.mean(mahnoor_base[:,0]))
avg=mahnoor.mean(mahnoor_baseball[:,0])
print("average hieght:"+str(avg))
#print median of first row
med=mahnoor.median(mahnoor_baseball[0,:])
print("median of weight is:"+str(med))
#print stddev of the heights
stdev=mahnoor.std(mahnoor_baseball[:,0])
print("stddev is:"+str(stdev))
#print correlation between height and weight as for correlation the size of the arrays should be same
corr=mahnoor.corrcoef(mahnoor_baseball[0,:],mahnoor_baseball[0,0:])
print("correlation:"+str(corr))
