# import numpy as np

# # list = [1,2,3,4]
# list = [[1,2,3],[4,5,6],[7,8,9]]
# arr = np.array(list)
# # print(type(list),list)
# # print(type(arr),arr)
# # arr = np.arange(1,7).reshape(2,3)
# # print(arr.ndim)#tells the dimension
# # print(arr.shape)
# # print(arr.size)
# # print(arr.itemsize)
# # print(arr)
# # print('\n')

# # ar = np.zeros((4,4))
# # ar = np.ones((4,4))
# # print(ar)

# '''INDEXING'''
# # l = [1,2,3,4]
# # ar = np.array(l)
# # print(ar[-2])
# # print(ar[2])
# # print(arr[1,2])
# # print(arr[1:2])
# # print(arr[1:])

# # print(arr[1:3,1:3])

# '''ARTHEMATIC OPERATIONS'''
# l1 = [[9,7],[1,0]]
# l2 = [[1,1],[1,1]]
# a = np.array(l1)
# b = np.array(l2)

# # print(a+b)
# # print('\n')
# # print(a-b)
# # print('\n')
# # print(a@b)
# # print('\n')
# # print(a//b)#for floor function.
# # print(a)
# # print('\n')
# # x = a.transpose()
# # print(x)

# '''SORTING'''
# l3 = [4,5,2,3,1]
# x = np.array(l3)
# print(x)
# print('\n')
# z = np.argsort(x)#gives the privious indexes of the array(1-D)before sort or if not sorted gives index in soted order
# # y = np.sort(x)
# # print(y)

# print(z)

import pandas as pd

# data = { 'Name' : ['sparsh','shiva','umesh','mohit'], 'Age'  : [11,33,44,55], 'City' : ['alwar','jharkhand','jaipur','jaipur']}

# df = pd.DataFrame(data)
# print(df)

data = [['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles'], ['Charlie', 35, 'Chicago'],['rohan', 35, 'Chicago'],['jhon', 35, 'Chicago'],['shovam', 35, 'Chicago']]
columns = ['Name', 'Age', 'City']

df = pd.DataFrame(data, columns=columns)
print(df)
# print(df.head())  # First 5 rows
# print(df.tail())  # Last 5 rows
# print(df.shape)  # (rows, columns)
# print(df.columns)
# print(df['Age'])  # Access the 'Age' column
# print(df.iloc[0])  # Access the first row
filtered_df = df[df['Age'] > 30]  # Filter rows where Age > 30
# print(filtered_df)

df['Salary'] = [50000, 60000, 70000,6564644,6546461,646212164]
# print(df)

df['Age'] = df['Age'] + 1  # Increment all ages by 1
print(df)
df.drop('Salary', axis=1, inplace=True)
print(df)

df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Salary': [50000, 60000, 70000]})

merged_df = pd.merge(df1, df2, on='ID')
print(merged_df)


# df = pd.read_csv('C:\\Users\\admin\\Desktop\\laptops.csv')  # Replace 'data.csv' with your file path
# print(df.head())  # Show first 5 rows
