# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 10:38:08 2021
@author: jami
"""
print(" Task 1: Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.")
print('\n')
import numpy.matlib
import numpy as np
y = range(10,22)
a = np.array(y)
print(a)
b = a.reshape(3,4)
print(b)
print('\n')
'One liner'
print( np.arange(10,22).reshape(3,4) )

###################################

print('\n')
print(" Task 2Write a NumPy program to test whether none of the elements of a given array is zero.")
print('\n')

a =np.array([0,1,2])
b =np.array([1,2,3])
c =np.array([0,1,2,3,0])

def Has_zero(array):
    data = 0 in array
    print("Array has zero") if data == True else print("Array has no zero")
Has_zero(a)
Has_zero(b)
Has_zero(c)

###################################

print('\n')
print("Task 3: Write a NumPy program to create an array with the values 1, 7, 13, 105 \n and determine the size of the memory occupied by the array. ")
print('\n')

from sys import getsizeof
a = [1,7,13,105]
b = np.array(a)
print(b)
print(getsizeof(b)) #120 bytes
print(b.nbytes)     #16 bytes 
c = np.matrix(a)
print(c)
print(getsizeof(c)) #144 bytes
print(c.nbytes)     #16 bytes 
## elements size stay(values) the same but format changes from a array to matrix

###################################

print('\n')
print("Task 4 Write a NumPy program to create an array of the integers from 30 to 70 ")
print('\n')

y = range(30,71)
a = np.array(y)
print(a)

###################################

print('\n')
print("Task 5: Write a NumPy program to reverse an array (first element becomes last). ")
print('\n')

array = np.array((1,2,3))
print(array)
array2 = np.flip(array)
print(array2)


###################################

print('\n')
print("Task 6:Write a NumPy program (using numpy) to sum of all the multiples of 3 or 5 below 100. ")
print('\n')
a = list(range(3,100,3)) 
b = list(range(5,100,5))
c = a + b
# there are dublicates now like 30
d = list(set(c)) #remove dublicates using set
np.array(d)
print (d)
print(sum(d))
## Better way?
k = np.arange(1,100)
z= k[(k % 3 == 0) | (k % 5 == 0)]
# check using modulo if has 0 left
print(z)
print(sum(z))

###################################

print('\n')
print(" Task 7: Add the following two NumPy arrays and Modify a result array by calculating the square root of each element")
print('\n')

arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])
arrayThree = np.add(arrayOne,arrayTwo)
print(arrayOne)
print('\n')
print(arrayTwo)
print('\n')
print(arrayThree)
arrayFour = np.sqrt(arrayThree)
print(arrayFour)
###################################

print('\n')
print("Task 8 Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10")
print('\n')

list100to200 = list(range(100,200,10)) 
array5x2 = np.array(list100to200)
array5x2 = array5x2.reshape(5,2)
print(array5x2)

###################################

print('\n')
print(" Task 9: Following is the 2-D array. Print max from axis 0 and min from axis 1")
print('\n')
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print('This is the array: \n', sampleArray)
print('\n')
print('This is the max in axis 0: \n',np.amax(sampleArray,axis=0 ))
print('\n')
print('This is the min in axis 1: \n',np.amin(sampleArray,axis=1 ))

###################################

print('\n')
print("Taskk 10: Sort following NumPy array  \n1. by the second row and \n2. by the second column")
print('\n')
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
print('Sample array: \n',sampleArray , '\n')

a = sampleArray[sampleArray[1, :].argsort()]
print('Sorted by row 2:\n' , a)
b = sampleArray[sampleArray[:, 1].argsort()]
print('Sorted by colum 2:\n' , b)
