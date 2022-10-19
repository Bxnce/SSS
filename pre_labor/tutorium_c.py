# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
from numpy import *

#vector
v = array([1,2,3,4])

#matrix
m = array([[1,2],[3,4]])

#m[0,0] = "hello" error because of fix types in vectors and matrix

#matrix with fix with prefixed datatype
m = array([[1,2],[3,4]], dtype=complex)

#create a ranged vector
x = arange(0, 10, 1) # arguments: start, stop, step

#create mesh grid
x, y = mgrid[0:5, 0:5]

#random data
x = random.rand(5, 5) #creates 5x5 matrix with random data range from 0-1

#standard normal distributed data
x = random.randn(5, 5)

#diagonal matrix
x = diag([1,2,3])

#diagonal matrix with offset from the main diagonal
x = diag([1,2,3], k=1)

#3x3 matrix filled with (float?) zeros
x = zeros((3, 3))

#3x3 matrix filled with (float?) ones
x = ones((3, 3))

#create from text files
data = genfromtxt("stockholm_td_adj.dat")

#create figure out of data
fig, ax = plt.subplots(figsize=(14,4))
ax.plot(data[:,0]+data[:,1]/12.0+data[:,2]/365, data[:,5])
ax.axis('tight')
ax.set_title('temperature in Stockholm')
ax.set_xlabel('year')
ax.set_ylabel('temperature (C)')
 
#using numpy.savetxt to store a Numpy array to file in CSV format
m = random.rand(3,3)

savetxt("random-matrix.csv", m, fmt='%.5f') #fmt is format

save("random-matrix.npy", m) #save as numpy native file
x = load("random-matrix.npy")

#assign value to a whole row
m[1, :] = -1

#assign value to a whole column
m[:, 1] = 1

#print whole row/column
#print(m[1, :]) # print row with index 1
#print(m[:, 1]) # print column with index 1

#Index slicing
A = array(range(1,6))
A_slice = A[1:3] 

#change value of slice
A[1:3] = [-2, -3]
A_slice = A[1:3]

# A[lower:upper:step] negative indices count from the end to the start
A_slice_first = A[:3] #first 3 elements
A_slice_second = A[3:] #elements from index 3 to the end
A_slice_third = A[-1] #last element
A_slice_fourth = A[-3:] #last 3 elements

#index slicing with matrix
A = array([[n+m*10 for n in range(5)] for m in range(5)])

A_slice = A[1:4, 1:4] #slices rows 1-3 and columns 1-3
A_slice = A[::2, ::2] #every second row and column

#fancy indexing
row_indices = [1,2,3]
A_slice = A[row_indices]
col_indices = [1,2,-1]
A_slice = A[row_indices, col_indices]


#masking
x = arange(0, 10, 0.5)
mask = (5 < x) * (x < 7.5) # \*=& operator

#where function
indices = where(mask)


#diag function  extracts diagonal and subdiagonal from matrix
diagonal = diag(A)
diagonal = diag(A, -1) #offset one to the left

#take 
row_indices = [1, 3, 5]
take_function = take([-3, -2, -1,  0,  1,  2], row_indices)

#choose
which = [0, 0, 1, 1]
choices = [[-2,-2,-2,-2], [5,4,5,5]]

result = choose(which, choices)

#array operations
v1 = arange(0, 5)
v1_2 = v1 * 2 #multiply each element by 2
v1_2 = v1 + 2 #add 2 to each element
V1_2_matrix  = A * 2, A + 2 # on matrix
a_times_a = A * A #element-wise multiplication
v1_times_v1 = v1 * v1
a_times_v1 = A * v1 #row multiplication, v1 gets multiplied on every row of A


#Matrix algebra
matrix_multiplication = dot(A, A)
matrix_multiplication = dot(A, v1)
matrix_multiplication = dot(v1, v1)

#cast to matrix
M = matrix(A)
v = matrix(v1).T #make it a column vector

#inner product
prod = v.T * v

#standard matrix algebra if the shape isn't compatible we will get an error 5x5 Matrix will not fit on 1x5 matrix
stand_res = v + M*v

#Array/Matrix transformations
C = matrix([[1j, 2j], [3j, 4j]])
negated_c = conjugate(C)

#hermitian conjugate = transpose + conjugate
hermitian_c = C.H

#extract real and imaginary part of the complex number
real_part = real(C)
imag_part = imag(C)

#Data processing
mean_temp = mean(data[:,3])

#Standard deviation and variance
std_dev = std(data[:,3])
std_var = var(data[:,3])

#min and max
min = data[:,3].min()
max = data[:,3].max()

d = arange(0, 10)
#sum of all elements
sum_d = sum(d)
#product of all elements
#prod_d = prod(d+1) #just stopped working :0   
#cummulative sum
cum_d = cumsum(d)
#cummulative product
cum_prod_d = cumprod(d+1)
# same as: diag(A).sum() sum of diagonal
print(array([[1,2],[3,4]]))
trace_d = trace(array([[1,2],[3,4]]))

#Computation on subsets of arrays
mask_feb = data[:,1] == 2
mean_feb = mean(data[mask_feb, 3])

months = arange(1,13)
monthly_mean = [mean(data[data[:,1] == month, 3]) for month in months]

fig, ax = plt.subplots()
ax.bar(months, monthly_mean)
ax.set_xlabel("Month")
ax.set_ylabel("Monthly avg. temp.");

#calculations with higher dimensional data
m = random.rand(3,3)
m_max = m.max() #global max from matrix
m_max_column = m.max(axis=0) #max from each column
m_max_row = m.max(axis=1) #max from each row


print(mean_feb)