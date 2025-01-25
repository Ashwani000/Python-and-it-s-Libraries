#Creation of data frames in pandas
import pandas as pd
'''data = {"Name" : ["John","Peter","Lisa"],"Age":[25,28,31],"Salary":[300000,40000,50000]}
df=pd.DataFrame(data)
print(df)

data=pd.read_csv("industry.csv")
print(data)'''
#install openpyxl library
'''data=pd.read_excel("FSI-2023-DOWNLOAD.xlsx")
print(data)'''

#exploring Data in pandas
'''data=pd.read_excel("Orders-With Nulls.xlsx")
print(data.head(10))  #give upper 10 values
print(data.tail(10))  #give lower 10 values
print(data.info())    #give all the information related to data
print(data.describe())  #it give all the mean median and other details of the data.
print(data.isnull().sum())
'''
#Handling duplicate values in pandas
'''data=pd.read_csv("industry.csv")
print(data)
print(data.duplicated())
print(data.drop_duplicates())  #delete the duplicate values from the data
'''
#working with missing data in pandas
'''
data=pd.read_csv("industry.csv")
print(data.isnull().sum())  #show null values
print(data.dropna())  #eliminate null values
print(data.replace(np.nan,"hi"))  #it replace all the values from the null values.
#forward fill or backword fill
print(data.fillna(method="ffill"))
print(data.fillna(method="bfill"))'''

#column Transformation in pandas
#--- in this we can add extra columns based on the the conditions.
'''df=pd.read_excel("Orders-With Nulls.xlsx")
#print(data)
df.loc[(df["Customer Segment"] == "Corporate"),"cxtype"] = "yes"
df.loc[(df["Customer Segment"] == "Small Business"),"cxtype"] = "No"
print(df.head(10))'''

#concatenate of two columns
'''data=pd.read_csv("industry.csv")
print(data)
#data["new column name"]= data["existing column1"] + data["existing column2"]'''

'''data=pd.read_excel("employee.xlsx")
print(data)
data["Full name"]= data["First Name"] + " " + data["Last name"]
print(data)
data['Bonus']=(data["Salary"]/100)*20
print(data)'''

'''data={"Months":["january","February","March","April"]}

a=pd.DataFrame(data)
print(a)
def extract(value):
    return value[0:3]
a["short Month"] = a["Months"].map(extract)
print(a)'''

#Group By in Pandas
'''data=pd.read_excel("employee.xlsx")
print(data)
gp=data.groupby(["column1,column2"]).agg({"column":"count"})'''

#Merge, Join, and concatenate in pandas
'''data1={"Empid":["E01","E02","E03","E04","E05"],"Names":["Ram","john","shyam","Alia","Tom"]
       ,"Age":[34,54,23,15,67]}
data2={"Empid":["E01","E02","E03","E04","E05"],"Salary":[45000,35000,20000,67000,65000]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(df1)
print(df2)
#merge based on left and right tables
print(pd.merge(left=df1,right=df2,on="Empid",how="left"))
#pandas has no attribut join
#print(pd.join(left=df1,right=df2,on="Empid",how="left"))'''

#concatenation
'''data1={"Empid":["E01","E02","E03","E04","E05"],"Names":["Ram","john","shyam","Alia","Tom"]
       ,"Age":[34,54,23,15,67]}
data2={"Empid":["E06","E07","E08","E09","E10"],"Names":["Rom","jon","sham","lia","bom"]
       ,"Age":[34,54,23,15,67]}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)
print(pd.concat([df1,df2]))'''

#compare DataFrames
'''dict={"Fruits":["MAngo","Apple","pear","papaya"]
      ,"Price":[100,150,60,80],"Quantity":[15,10,10,3]}
df=pd.DataFrame(dict)
print(df)
df2=df.copy()
df2.loc[0,"Price"]=120
df2.loc[1,"Price"]=240
df2.loc[3,"Price"]=140
df2.loc[0,"Quantity"]=12
df2.loc[1,"Quantity"]=15
df2.loc[3,"Quantity"]=4
print(df2)
 
#keep shape= return Nan where no changes
print(df.compare(df2,))'''

#pivoting and melting DataFrames
'''dict={"keys":["k1","k2","k1","k2"],
      "Names":["Rom","jon","sham","lia"],
      "House":["red","blue","green","yellow"]}
df=pd.DataFrame(dict)
print(df)
print(df.pivot(index="keys",columns="Names",values="House"))
'''

#Melting
'''dict={"keys":["k1","k2","k1","k2"],
      "Names":["Rom","jon","sham","lia"],
      "House":["red","blue","green","yellow"],
      "Grades":["3rd","4rth","5th","6th"]}
df=pd.DataFrame(dict)
print(df)
print(pd.melt(df,id_vars=["Names"],value_vars=["Grades","House"],var_name="House&Grades",value_name="values"))
'''


