import seaborn as s
import pandas as pd
import matplotlib.pyplot as plt

#line plot
'''data={"days":[1,2,3,4,5],"NOP":[50,60,20,30,70]}
df=pd.DataFrame(data)
print(df)
s.lineplot(data=data,x="days",y="NOP")
plt.show()'''

#bar plot
'''data= s.load_dataset("tips")
print(data)
s.barplot(data=data,x="day",y="tip",estimator="median",hue="sex",palette="viridis",order=["sun","sat","fri","Thu"])
plt.show()'''

#Hist plot
'''data=s.load_dataset(("tips"))
s.histplot(data,x="day",hue="sex",kde=True)
plt.show()'''

'''data=s.load_dataset(("titanic"))
s.histplot(data, x="age",hue="sex",kde=True)
plt.show()'''

#scatter plot

'''data=s.load_dataset("tips")
s.scatterplot(data=data,x="total_bill",y="tip",hue="sex")
plt.legend(bbox_to_anchor=(0.2,0,1.2,1)) #x,y,width,height
plt.show()'''

#heatmap plot
'''data=s.load_dataset("tips")
print(data)
gp=data.groupby("day").agg({"total_bill" : "sum"})
s.heatmap(gp)
plt.show()'''

#CountPlot

'''data=s.load_dataset("tips")
print(data)
s.countplot(data=data,x="day",hue="sex")
plt.show()'''

#violin plot -- it plot on numerical plot

'''data=s.load_dataset("tips")
s.violinplot(data=data,x="total_bill")
plt.savefig("violin.png")
plt.show()'''

#pair plot

'''data=s.load_dataset("tips")
s.pairplot(data,hue="day")
plt.savefig("pairplot.png")
plt.show()'''

#strip plot

'''data=s.load_dataset("tips")
s.stripplot(data=data,x="day",y="total_bill",jitter=0.3)
plt.show()'''

#BoxPlot

'''data=s.load_dataset("tips")
s.boxplot(data=data,x="day",y="tip",orient="vertical")
plt.show()'''

#cat plot-- category plot

'''data=s.load_dataset("tips")
s.catplot(data=data,x="day",y="tip",kind="violin")
plt.show()'''

#style and color in seaborn

'''data=s.load_dataset("exercise")
s.set_style(style="darkgrid")
s.barplot(x="time",y="pulse",data=data)
plt.show()

data=s.load_dataset("exercise")
s.set_style(style="ticks")
s.barplot(x="time",y="pulse",data=data)
plt.show()


s.palplot(s.color_palette("viridis"))
plt.show()'''

#Multiple plots in seaborn

'''data=s.load_dataset("tips")
a=s.FacetGrid(data,col="smoker")
a.map(s.barplot,"day","tip")
plt.show()'''

#Relational Plot in seaborn
'''data=s.load_dataset("tips")
s.relplot(data=data,x="tip",y="total_bill",hue="sex",kind="line",col="day",size="smoker")
plt.show()'''

#swarm plot

'''data=s.load_dataset("tips")
s.swarmplot(data=data,x="day",y="total_bill")
plt.show()'''

#KDE Plot
data=s.load_dataset("tips")
s.kdeplot(data=data,x="total_bill")
plt.show()


