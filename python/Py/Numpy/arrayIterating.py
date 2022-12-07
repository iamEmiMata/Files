
import numpy as np


# 2d 
arr = np.array([[1,2,3], [2,4,6]])

for x in arr:
	for y in x:
		print(y)


print('\n')

# 3d 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z, end =',')

print('\n')

# nditer
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)

print('\n')

# skipping 1 num
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)


