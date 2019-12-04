import numpy as np

# a = np.array([1, 2, 3])   # Create a rank 1 array
# print(type(a))            # Prints "<class 'numpy.ndarray'>"
# print(a.shape)            # Prints "(3,)"
# print(a[0], a[1], a[2])   # Prints "1 2 3"
# a[0] = 5                  # Change an element of the array
# print(a)                  # Prints "[5, 2, 3]"

# b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
# print(b.shape)                     # Prints "(2, 3)"
# print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"
# print(b)

# a = np.zeros((2,2))   # Create an array of all zeros
# print(a)              # Prints "[[ 0.  0.]
#                       #          [ 0.  0.]]"

# b = np.ones((1,2))    # Create an array of all ones
# print(b)              # Prints "[[ 1.  1.]]"

# d = np.eye(5)         # Create a 2x2 identity matrix
# print(d)              # Prints "[[ 1.  0.]
#                       #          [ 0.  1.]]"

# e = np.random.random((2,2))  # Create an array filled with random values
# print(e)                     


# Linear algebra

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(x)
print(v.T)
# print(w)
# print(v.dot(w))
# print(np.dot(v, w))

# # Matrix / vector product; both produce the rank 1 array [29 67]
# print(x.dot(v))
print("Result of matrix-vector mul is: ", np.dot(x, v))

# # Matrix / matrix product; both produce the rank 2 array
# # [[19 22]
# #  [43 50]]
# print(x.dot(y))
print(np.dot(x, y))
