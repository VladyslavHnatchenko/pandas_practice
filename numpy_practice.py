import numpy as np
from io import BytesIO


data = "1,2,3\n4,5,6"
res = np.genfromtxt(BytesIO(data.encode()), delimiter=",")
print(res)
# a = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
# print(a.cumsum(axis=0))

# print(a.sum(axis=1))

# a = np.random.random((2, 5))
# print(a)

# a = np.ones(5)
# print(a)

# a = np.arange(5)
# print(np.sqrt(a))
# a = np.array([1, 2, 3, 4, 5])
# b = np.array([6, 7, 8, 9, 10])
# c = a.copy()
# c[:] = 10
#
# print(c)
# print(a)

# print(a * b)
# print(a > 2)

# arr = np.array([2.3, 4.5])
# print(arr.dtype)

# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# arr2 = np.arange(0, 10).reshape(5, 2)

# print(arr)
# print(arr2)
