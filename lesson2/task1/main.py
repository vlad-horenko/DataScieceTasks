import numpy as np
import math

n = int(input('Enter number of points: '))

A = np.random.uniform(low=-1, high=1, size=(n,2))
count = 0
for index, element in enumerate(A):
    hypotenuse = math.sqrt(A[index][0] ** 2 + A[index][1] ** 2)
    if hypotenuse <= 1:
        count +=1
print(f'{count} points are included in the unit circle from all given points.')
print(f'X = {count*4/n}')
