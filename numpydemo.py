from statistics import correlation

import numpy as np
import statistics as stats
'''a=np.array([20,30,40])
b=np.array([60,70,80])
print(a)  #it convert list to array
print(b)
print(a+b)   #it perform direct operation in an array.
print(a*b)'''
''''#for single dimension slicing
arr= np.array([10,20,30,40],)
print(arr[2:])

#for multi dimension
arr= np.array([[10,20,30,40],[50,60,70,80]])
print(arr[0:2,0:2])
#if we want only middle values from first array
print(arr[0,1:3])
#if we want rows and columns of an array
print(np.shape(arr))
#if we want total number of elements in an array
print(np.size(arr))
#find the dimension of an array
print(np.ndim(arr))
#find datatype of an array
print(arr.dtype)
print(type(arr))
print(arr.shape)
#convert datatype
print(arr.astype(float))'''
#Mathematical Operations and Functions on Array
#for  on dimensional array
'''arr1= np.array([30,40,50,60])
arr2=np.array([60,70,80,90])
print(arr1+arr2)
print(np.add(arr1,arr2))'''
#for two dimensional array
'''arr1=np.array([[30,40],[20,10]])
arr2=np.array([[30,20],[10,20]])
print(arr1+arr2)
print(np.add(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))'''
#for power and square root

'''arr1=np.array([3,4,5,6])
arr2=np.array([2])
print(np.power(arr1,arr2))
arr3=np.array([ 9 ,16 ,25, 36])
print(np.sqrt(arr3))'''

#combination and spliting arrays
#concatenate
'''arr1= np.array([[30,40],[50,60]])
arr2=np.array([[6,5],[7,2]])
print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2],axis=1))
#horizontal concantenate
print(np.hstack([arr1,arr2]))
#vertical concatenate
print(np.vstack([arr1,arr2]))'''

#slpiting of value
'''a=np.array([1,2,8,5])
b=np.array_split(a,3)
print(b)'''
'''
#Adding and Removing elements in the Array
#append
arr1=np.array([3,4,5,6])
print(np.append(arr1,90))
arr2= np.array([[30,40],[50,60]])
print(np.append(arr2,90))
#insert
print(np.insert(arr1,1,100)) #np.insert(array,index,value)
#delete
print(np.delete(arr1,1))
'''
'''
#sort,filter and search in NUmpy
#1. sort
arr1=np.array([[8,3,4,7,2,5,6],[2,8,3,7,5,6,1]])
print(np.sort(arr1))
#search
arr1=np.array([8,3,4,7,2,5,6])
s=np.where(arr1%2==0)
print(s)
#search sorted
arr1=np.array([1,2,3,4,5,6,7])
ss=np.searchsorted(arr1,5)
print(ss)
#filter

arr1= np.array([30,40,50,60])
fa = [True, False,True,False]  #give only true value as output
new=arr1[fa]
print(new)

fa=arr1>35
new1=arr1[fa]
print(new1)
'''

#aggregating functions in Numpy
'''a= np.array([30,40,50,60])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))  #count no. of values
print(np.mean(a))
print(np.cumsum(a)) #cummulative sum 30, 30+40, 30+40+50......
print(np.cumprod(a))'''

'''
a=[100,400,600,900,200,600,100]
b=[10,50,30,40,50,70,20]
price=np.array(a)
quantity=np.array(b)
print(price,"\n",quantity)
c=np.cumprod([price,quantity],axis=0)
print(c[1].sum())
'''
#statiscal functions in numpy
'''baked_food=[200,300,150,130,200,280,170,180]
a=np.array(baked_food)
print(np.mean(baked_food))  #sum of all the values/number of values
print(np.median(baked_food))  #sort the values and find the mid value and average of it
print(stats.mode(baked_food))  #most occuring value
print(np.std(baked_food))  #standard deviation
print(np.var(baked_food)) #variation  '''

#coeffiencient of correlation  -1 represent inversely proportinal relationship
#+1 represnt proportional relationship
#0 means no relationship
'''tobacco_consumption = [30,50,10,30,50,40]
deaths=[100,120,70,100,120,112]
print(np.corrcoef([tobacco_consumption,deaths]))

price=[300,100,350,150,200]
sales=[10,20,7,15,3]
print(np.corrcoef([price,sales]))'''