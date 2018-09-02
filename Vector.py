# Load library
import numpy as np

# Create vector
vector = np.array([1, 2, 3, 4, 5, 6])

# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10,11,12]])


print(vector.transpose())
print(matrix.transpose())

#############Selecting Elements In An Array ###############

# Select second element. ALways start from 0
print(vector[1])

# Select second row, second column
print(matrix[1,1])

###### Create Tensor########
# Create matrix
tensor = np.array([
                    [[[1, 1], [1, 1]], [[2, 2], [2, 2]]],
                    [[[3, 3], [3, 3]], [[4, 4], [4, 4]]]
                  ])

# Select second element of each of the three dimensions
print(tensor[1,1,1])

########### Reshape Array  ################
# Reshape matrix into 2x6 matrix
print(matrix.reshape(2, 6))

########### Invert A Matrix
matrix = np.array([[4, 7],
                   [2, 6]])

print(np.linalg.inv(matrix))

