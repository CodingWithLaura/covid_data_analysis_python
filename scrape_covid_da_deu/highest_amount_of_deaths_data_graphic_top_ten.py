import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt 
import pandas
import pylab as plt

cmap=plt.get_cmap("jet")

all_deaths = pandas.read_csv('Todesfaelle_Corona_2021-10-01.csv').values

last_index = len(all_deaths[0]) - 1
permutations_array = all_deaths[:,last_index].argsort()
all_deaths = all_deaths[permutations_array]
all_deaths = all_deaths[::-1]
kreis_array = all_deaths[0:9,4]
top10_death_arrays = all_deaths[0:9]

numdays = len(all_deaths[0][6:])
base = dt.datetime.fromisoformat('2020-03-01')
date_list = [base + dt.timedelta(days=x) for x in range(numdays)]

N=10
for i in range(0,9):
    mycolor = cmap(i/N)
    plt.plot(date_list, top10_death_arrays[i][6:],color=mycolor,label=kreis_array[i])
    
plt.legend()
plt.show()



