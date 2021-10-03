import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt 

#optimized version
test_data = genfromtxt('todesfall_daten_homogen.csv', delimiter=',')
all_deaths = genfromtxt('total_deaths_homogene.csv', delimiter=',')

last_index = len(all_deaths[0]) - 1
permutations_array = all_deaths[:,last_index].argsort()
all_deaths = all_deaths[permutations_array]
all_deaths = all_deaths[::-1] 
top10_death_arrays = all_deaths[0:9]

print(top10_death_arrays)   
numdays = len(test_data[0])
base = dt.datetime.fromisoformat('2020-03-01')
date_list = [base + dt.timedelta(days=x) for x in range(numdays)]

test_data_koeln = test_data[0]
test_data_ilm = test_data[1]

plt.plot(date_list,test_data_koeln,'r')
plt.plot(date_list,test_data_ilm,'g')
for i in range(0,9):
    plt.plot(date_list, top10_death_arrays[i],'b')

plt.show()

einwohner_koeln = 1086000
einwohner_ilmkreis = 108742

