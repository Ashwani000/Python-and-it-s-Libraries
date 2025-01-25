import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#bar plot -- use plt.bar to draw bar grap

'''y=[98,67,78,88,98]
x=["Part1","Part2","Part3","Part4","Part5"]
colors=["red","green","blue","yellow","brown"]
plt.bar(x , y, color= colors,edgecolor="black")
plt.xlabel("parts of harry porter",fontsize=20)
plt.ylabel("popularity")
plt.title("Harry porter")
plt.show()'''
#plot a bar through data reading
'''data=pd.read_excel("employee.xlsx")
df=pd.DataFrame(data)
print(df)
plt.bar(df["Empid"], df["Salary"], color="black")
plt.show()'''

#Lineplot -- use plt.plot for making line plot

'''x=["day1","day2","day3","day4","day5",]
y=[300,400,250,220,450]
y1=[500,450,300,250,320]
plt.plot(x,y,marker="o",ls=":",color="red",label="week1")
plt.plot(x,y1,marker="*",ls="--",color="green",label="week2")
plt.legend()
plt.show()'''
#plot on the basis of external data
'''data=pd.read_excel("employee.xlsx")
df=pd.DataFrame(data)
print(df)
plt.plot(df["Empid"], df["Salary"], color="black")
plt.show()'''

#scatter plot -- plt.scatter to print scatter plot
'''x=np.random.randint(1,10,50)
y=np.random.randint(10,100,50)
color=np.random.randint(10,100,50)
plt.scatter(x,y,marker="*",cmap="hot",c=color)
plt.colorbar()
plt.show()'''
'''data=pd.read_excel("employee.xlsx")
#color=np.random.randint(1,10,5)
df=pd.DataFrame(data)
print(df)
plt.scatter(df["Empid"], df["Salary"],marker="*",cmap="hot")
plt.show()'''

#Pie chart
'''brand=["vivo","oneplus","oppo","Nokia","MI"]
x=[10,40,25,22,45]
c=["red","blue","green","yellow","purple"]
ex=[0,0,0,0,0.1]
plt.pie(x, labels=brand,colors=c,pctdistance=0.6,explode=ex,shadow=True,autopct="%.2f",startangle=90)
plt.show()'''
'''data=pd.read_excel("employee.xlsx")
#color=np.random.randint(1,10,5)
df=pd.DataFrame(data)
c=["red","blue","green","yellow","purple"]
print(df)
plt.pie(df["Salary"], colors=c,pctdistance=0.6, shadow=True,autopct="%.2f",startangle=90)
plt.show()'''

#Box Plot -- in this, min value(lower Fence)-Q1-25%-median-Q3-75%-Max(upper fence)
#Q1=25/100*(n+1), n= no of values
#min fence=Q1-1.5(IQR)  max=Q3-1,5(IQR)
'''l=[25,46,57,25,45,13,39,46,200,22,12,14,16,55,23,55,78]
plt.boxplot(l)
plt.show()'''

#Histogram plot-- it is used to know the frequency of data
'''x=[30,40,68,47,84,57,5,6,2,5,7,50,60]
plt.hist(x,bins=13,edgecolor="black", color="pink")
plt.show()'''

#violin plot
'''x=[30,40,68,47,84,57,5,6,2,5,7,50,60]
plt.violinplot(x,showmedians=True)
plt.show()'''

#Stem plot
'''x=[30,40,68,47,84,57,5,6,2,5,7,50,60,30,68,30,47]
plt.stem(x)
plt.show()'''

#Stack plot
'''days=[1,2,3,4,5,6,7]
NOP1=[5,10,30,20,35,60,80]
NOP2=[10,20,30,40,50,70,89]
NOP3=[8,16,24,32,40,56,100]
plt.stackplot(days,NOP1,NOP2,NOP3)
plt.show()'''

#Step plot
'''x=["day1","day2","day3","day4","day5",]
y=[10,20,30,40,50]
plt.step(x,y )#where: Literal["pre", "post", "mid"])
plt.show()'''

#working with legends
'''x=[1,2,3,4,5]
y=[45,67,33,67,12]
y1=[41,62,83,66,13]
plt.plot(x,y,label="male")
plt.plot(x,y1,label="female")
plt.legend(loc=3)
plt.show()'''

#subplot

x=[1,2,3,4,5]
y=[23,45,65,24,15]
plt.subplot(1,2,1) #rows,columns,chart number
plt.plot(x,y)

plt.title("AGE")
x=[5,6,7,8,9]
y=[45,35,24,56,76]
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("weight")
plt.suptitle("Employee data")
plt.savefig("plot.png",facecolor="green")
plt.show()


