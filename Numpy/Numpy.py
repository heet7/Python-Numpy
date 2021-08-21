
import numpy as np

# Create a list
l = [ [1,2] , [3,4] ]

# convert into matrix and store into a
a = np.array(l)
a

# what happen when a + a = ?
# cordinate wise addition , substration.
a+a

# what about multiplacation..?
# what is the minimin condition to multiply two matrix?
# answer : Rows in the first matrix should be equal to the columns of secound martix..
# [ [ 1 , 2] ,   [ [ 1 , 2 ],        [ [ 5 , 8 ]
#              x               = 
#   [ 2 , 3]]      [ 2 , 3 ] ]         [ 8 , 13 ] ]
a = np.array ([[1,2],[2,3]])

# there is 2 ways to multiply matrix

# 1
np.dot(a,a)

# 2
np.matmul(a,a)

a.shape

# inverce calculation
# -properties
#  -->let's check identity matrix is always looks like this..
# [1. , 0.],
# [0. , 1.]

# inverce matrix calculation
np.linalg.inv(a)

# let's check calculation is right or not
np.dot(np.linalg.inv(a),a)

# =======================================================

# all the basic mathamatical function is stored in numpy

np.sin(10)

np.exp(10)

np.log(10)

# =======================================================


# Rotate a with respect to Rows
#          with respect to Columns
a = np.array([[1,2],[3,4]])
a[: : -1 , : : -1]

# access one row
a[0,:]

# access entire first column
a[:0]

# access last column
a[:,-1]
# or
a[:,1]


