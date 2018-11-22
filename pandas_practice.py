import numpy as np
import pandas as pd


index1 = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
index2 = [1, 2, 3, 1, 2, 3]
mix_index = list(zip(index1, index2))
mix_index = pd.MultiIndex.from_tuples(mix_index)

df = pd.DataFrame(np.random.randn(6, 3), mix_index, ['A', 'B', 'C'])
# print(mix_index)
# print('\n')
print(df)


# arr = np.arange(0, 9).reshape(3, 3)
# df = pd.DataFrame(arr, ['A', 'B', 'C'], ['X', 'Y', 'Z'])
# df['H'] = [4, 4, 4]
# df.drop('H', axis=1, inplace=True)
#
# con1 = df > 2
#
# print(df[con1])

# arr = np.arange(0, 9).reshape(3, 3)
# df = pd.DataFrame(arr, ['A', 'B', 'C'], ['X', 'Y', 'Z'])
# df['new'] = df['X'] + df['Y']
# print(df)
# # print(df)
# print(df.loc('A'))

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
#
# df = pd.DataFrame(arr, ['A', 'B', 'C'], ['X', 'Y', 'Z'])
# print(df)

# index = ["a", "b", "c", "d"]
# arr = np.array(["Tom", "Jerry", "Tony", "Spark"])
# ser = pd.Series(data=arr, index=index)
# print(ser)
