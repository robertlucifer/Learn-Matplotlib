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
#plt.pie(votes1,labels=lang, explode=explodes, autopct="%.0f%%", pctdistance=0.8, startangle=45)
#plt.show()

#------------------------------------------------------
#creating data for box plot
heights=np.random.normal(172,8,300)
#plt.boxplot(heights)    
#plt.show()
#------------------------------------------------------
# customize you plot with title, xlabel, ylabel, grid, fontname, fontsize, color.
year=[2014,2015,2016,2017,2018,2019,2020,2021]
income=[55,56,62,61,72,72,73,75]
plt.plot(year,income)
#plt.title adds the title to the plot, you can customize with fontsize, color, font-family and more.
plt.title("Income of the Robert", fontsize=20, color="red", fontname="Times New Roman")
#plt.xlabel is used to add labels to the x-axis, you can customize with fontsize, color, font-family and more. Same applies for the ylabel.
plt.xlabel("Year")
plt.ylabel("Income")
#plt.grid is used to plot the grid line in your plot.
plt.grid()
plt.show()
#------------------------------------------------------

#adding legends to the plot

sample1=np.random.randint(0,20,10)
sample2=np.random.randint(0,20,10)
sample3=np.random.randint(0,20,10)
plt.plot(sample1, label="sample 1")
plt.plot(sample2, label="sample 2")
plt.plot(sample3, label="sample 3")
#you have to add this plt.legend() to show the legends in the plot. you can change the position of the legend box using the loc attribute 
plt.legend(loc="lower center")
plt.show()
#------------------------------------------------------
#importing style sheet from matplotlib.

from matplotlib import style   
#this creates different style of plots.
style.use("ggplot")
style.use("dark_background")

#------------------------------------------------------

#creating multiple plots

x1, y1=np.random.randint(0,50,10),np.random.randint(0,50,10)
x2, y2=np.random.randint(0,50,10),np.random.randint(0,50,10)
plt.figure(1)
plt.plot(x1,y1)

plt.figure(2)
plt.plot(x2,y2)
#by adding multiple figures you can display both the plot in the sametime.
plt.show()

#------------------------------------------------------

#using axes to plot multiple plots in the same figure.
a=np.random.randint(0,50,10)
fig, axs=plt.subplots(2,2)
#using index you can plot multiple plots in a single figure.
axs[0,0].plot(a,a**2)
axs[0,1].plot(a,a**3)
axs[1,0].plot(a,a**4)
axs[1,1].plot(a,a**5)
#you can add title to each plot using set_title and by mentioning the index of that plot, you can use all the customzation.
axs[0,0].set_title("Square")
plt.savefig("plot.png",dpi=300,transparent=True)
plt.show()
#------------------------------------------------------

#saving the plot and dpi is used to mention the quality of the immage, and you can also add the transparent background.
