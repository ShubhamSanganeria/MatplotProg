import matplotlib.pyplot as plt 
import csv
import time
import numpy as np
t=time.clock()
date=[]
op=[]
cl=[]
'''
with open('/home/shubhams/Downloads/GOOG.csv','r') as csvfile:
	plots=csv.reader(csvfile,delimiter=',')
	for r in plots:
		date.append(r[0])
		op.append(r[1])
		cl.append(r[-2])
'''
date,op,cl=np.loadtxt('/home/shubhams/Downloads/GOOG.csv',delimiter=',',usecols=(0,1,-2),dtype=str,unpack=True )		



date=date[1:]
op=op[1:]
cl=cl[1:]
y1_axis=[]
y2_axis=[]
x_axis=[]


for i in range(0,len(date)):
	if date[i][5:7]=='02':
		x_axis.append(int(date[i][8:10]))
		y1_axis.append(float(op[i]))
		y2_axis.append(float(cl[i]))

plt.plot(x_axis,y1_axis,'r',label="OPEN DAY")
plt.plot(x_axis,y2_axis,'g',label="CLOSE DAY")
plt.legend()
plt.title("GOOGLE STOCKS OF FEB")
plt.xlabel("DAYS")
plt.ylabel("PRICE")



print(time.clock()-t)
plt.show()