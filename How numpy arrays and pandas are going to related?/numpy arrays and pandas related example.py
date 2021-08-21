
import numpy as np
import pandas as pd

a = np.array( [ [1,2],[3,4] ])
a

# how to get row wise mean
a.mean(axis=0)

# how to get columns wise maximum
a.max(axis=1)

# you can do all maximum,minumim,std,variance,etc...
# Now, if you have a data frame if you do this... you got matrix in the np array

b.values

a = {"name":['Heet',"jash"],"age":[22,20]}
b = pd.DataFrame(a,index=['R1','R2'])
b.columns=["c1","c2"]
b

b.values

# concatenate row wise matrix
a = np.array( [ [1,2],[3,4] ])
np.concatenate([a,a],axis=0)

#concatenate side by side
np.concatenate([a,a],axis=1)
