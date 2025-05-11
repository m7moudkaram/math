import numpy as np
# Create a 2D NumPy array
#shape (4, 5) with random integers between 10 and 100 using
arr=np.random.randint(1,100,size=(4,5))

#The shape and data type of the array.
shape=arr.shape
print("the shape of the array: ")
print(shape)
type=arr.dtype
print("the type of the array: ")
print(type)

# The sum of all elements in the array.
sum=np.sum(arr)
print("sum of all elements: ")
print(sum)

# Mean and standard deviation
mean=np.mean(arr)
standard_deviation=np.std(arr)

#maximum & minimum
max=np.max(arr)
min=np.min(arr)
print("the maximum element in the array is\n",max)
print("the minimum element in the array is\n",min)

# Slicing and Indexing
# First 2 row
rows=arr[:2]
print("the first 2 rows:\n",rows)

#the last 3 columns
columns=arr[:, -3:]
print("the last 3 columns\n",columns)

# even numbers in the array.
even=arr[arr%2==0]
print("even elements:\n",even)

# Boolean Masking
# Replace values <= 50 with 0
masked = np.where(arr > 50, arr, 0)
print("\nArray with values > 50 kept and others replaced with 0:\n", masked)

# Reshape to (2, 10)
reshape=arr.reshape(2,10)
print("reshaped array:\n",reshape)

#transposing
transpose=arr.transpose()
print("array after transposing:\n",transpose)