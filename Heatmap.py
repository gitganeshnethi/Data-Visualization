# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:28:27 2019

@author: Ganesh Nethi
"""
!pip install pydataset
from matplotlib import pyplot as plt
import seaborn as sb
import pandas as pd
from pydataset import data
plt.rcParams['figure.figsize'] = [10,8]

data() #gives inbuilt datasets
flights = sb.load_dataset('flights')
flights.head()

#converting the long data into wide data using reshape

wide_flights = flights.pivot(index='month',columns='year',values='passengers')
wide_flights.head()

#Heat map using matplotlib
plt.imshow(wide_flights,cmap='hot_r')
plt.xticks(range(len(wide_flights.columns)),wide_flights.columns)#x-axis should be columns of wide table
plt.yticks(range(len(wide_flights.index)),wide_flights.index)#y-axis should be index of wide table
plt.colorbar()
plt.show()

#Heat map using seaborn
sb.heatmap(wide_flights,cmap='hot_r',linewidths=0.5,annot=True,fmt='d')
