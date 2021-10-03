import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import datetime as dt 

test_data = genfromtxt('todesfall_daten_homogen.csv', delimiter=',')

numdays = len(test_data[0])
base = dt.datetime.fromisoformat('2020-03-01')
date_list = [base + dt.timedelta(days=x) for x in range(numdays)]

test_data_koeln = test_data[0]/10.86
test_data_ilm = test_data[1]/1.08742

plt.plot(date_list,test_data_koeln,'r')
plt.plot(date_list,test_data_ilm,'g')
plt.show()

einwohner_koeln = 1086000
einwohner_ilmkreis = 108742

#Todesfälle durch 10,86 in Köln = Todesfälle pro 10000
#~  ~             1,08742 in Ilm

