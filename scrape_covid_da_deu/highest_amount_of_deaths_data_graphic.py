import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt 

test_data = genfromtxt('todesfall_daten_homogen.csv', delimiter=',')
all_deaths = genfromtxt('total_deaths_homogene.csv', delimiter=',')

tupel_array_with_last_value = [(index, all_deaths[index][len(all_deaths[index])-1]) for index in range(len(all_deaths))]
tupel_array_with_last_value.sort(key=lambda tup: tup[1], reverse=True)
#print(type(tupel_array_with_last_value))
frst_index = tupel_array_with_last_value[0][0]    
top10_death_arrays = np.array([all_deaths[tupel_array_with_last_value[0][0]]])
for i in range(1,9):
    tupel = tupel_array_with_last_value[i]
    array_index = tupel[0]
    top10_death_arrays = np.append(top10_death_arrays, [all_deaths[array_index]], 0)

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

