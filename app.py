import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# creating random data for Scatter plot
X=np.random.randint(0,50,size=50)
Y=np.random.randint(0,50,size=50)
# Here the X and Y are the data which are used to plot the scatter plot.
# C is used to mention the color of the marker(color can be also mentioned with hexa decimal values). 
#Marker is used to change the marker style [o,*,+, s[square], v [triangle_down], ^ [triangle_up], <[triangle_left], > [triangle_right], p[pentagon], h [hexagon], D [diamond], d[thin_diamond], |[vertical line], _ [horizaontal line], x[x]. 
#S is used to mention the size of the marker. 
#Alpha is used to mention the transparency of the marker.
#plt.scatter(X,Y, c="red", marker="|", s=50,  alpha=0.5)
#plt.show()
#------------------------------------------------------

# creating data for line plot
years=[2006 + x for x in range(16)]
weights=np.random.randint(70,85,size=16)
#This is the default plot function. 
#All the markers in scatter can also used in line plot. 
#Line width can be defined using lw="size.
#Line style can be mention using linestyle="--""
#plt.plot(years,weights, c="red", marker="*",lw=5, linestyle="--")
#plt.show()
#------------------------------------------------------

#creating data for bar plot
pro=["C++","C","Java","Python","Ruby","Go,","Rust","Scala","Kotlin","Swift"]
votes=[100,90,80,70,60,50,60,70,60,100]
#Bar plot is used for catargorical data. 
#Same attributes can be used here. here the color should be mentioned as "color" not c.
# width is used me mention the width of each bar in the graph. 
#edge color is used to mention the border color of the bars.
#Linewidth is used to mention the width of the border.
#plt.bar(pro,votes, color="red", linewidth=2, edgecolor="green", width=0.5)
#plt.show()

#------------------------------------------------------

#creating data for Histogram
hist1=np.random.normal(20,1.5,1000)
#plt.hist(hist1,bins=20,cumulative=True)
#plt.show()

#------------------------------------------------------
#creating data for pie chart
lang=["C++","C","Java","Python","Ruby"]
votes1=[15,10,20,50,5]

explodes=[0,0,0,0,0.2]
plt.pie(votes1,labels=lang, explode=explodes, autopct="%.0f%%", pctdistance=0.8, startangle=45)
plt.show()

#------------------------------------------------------
#creating data for box plot
heights=np.random.normal(172,8,300)
plt.boxplot(heights)    
plt.show()
#------------------------------------------------------
