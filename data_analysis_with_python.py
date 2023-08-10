import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
print(a * b)


# Creating numpy array
arr = np.array([1, 2, 3, 4, 5])
print(type(arr))

print(np.zeros(10, dtype=int))
print(np.random.randint(0, 10, size=10))
print(np.random.normal(10, 4, (3, 4)))

# ndim: size number
# shape: size info
# size: total number of elements
# dtype: data type of array

a = np.random.randint(10, size = 5)
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# Reshape()
print(np.random.randint(1, 10, size=9).reshape(3, 3))

# Index Selection
b = np.random.randint(10, size=10)
print(b[0])
print(b[0:5]) # Slicing

c = np.random.randint(10, size=(3, 5))
print(c)
print(c[0, 0])

print(c[:, 0]) # all rows, 0th columns
print(c[0:2, 0:3])

# Fancy Index
v = np.arange(0, 30, 3)
print(v)
print(v[1])

catch = [1, 2, 3]
print(v[catch])

# Conditions on Numpy
e = np.array([1, 2, 3, 4, 5])

# With classical loop
ab = []
for i in e:
    if i < 3:
        ab.append(i)
print(ab)

# With Numpy
print(e[e < 3])
print(e[e > 3])
print(e[e != 3])
print(e[e == 3])
print(e[e >= 3])

# Mathematical Operations

x = np.array([1, 2, 3, 4, 5])
print(x / 5)
print(x * 5 / 10)
print(x ** 2)
print(x - 1)

print(np.subtract(x, 1))
print(np.add(x, 1))
print(np.mean(x))
print(np.sum(x))
print(np.min(x))
print(np.max(x))
print(np.var(x))

# Solving equation with two unknowns with NumPy
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

y = np.array([[5, 1], [1, 3]])
z = np.array([12, 10])

print(np.linalg.solve(y, z))
