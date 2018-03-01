import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
from urllib import request
import numpy as np 
import time

t=time.clock()
goog_url="https://pythonprogramming.net/yahoo_finance_replacement"

def byteToDate(fmt,encoding='utf-8'):
	strconv=mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s=b.decode(encoding)
		return strconv(s)
	return bytesconverter

def get_data(goog_url):
	dt=[]
	st=0
	str_data=request.urlopen(goog_url).read().decode().split('\n')
	#occ=[m.start() for m in re.finditer(',',str_data)]
	for lines in str_data:
		if "Date" not in lines:
			dt.append(lines)

	date,op,cl=np.loadtxt(dt,delimiter=",",usecols=(0,1,4),unpack=True,converters={0:byteToDate('%Y-%m-%d')})
	
	ax=plt.figure()
	ax1=plt.subplot2grid((1,1),(0,0))

	ax1.plot_date(date,op,'-',label="Opening curve")
	ax1.fill_between(date,op,op[25],where=(op>op[25]),facecolor='c',alpha=0.5)
	ax1.fill_between(date,op,op[25],where=(op<op[25]),facecolor='r',alpha=0.5)


	for i in ax1.xaxis.get_ticklabels():
		i.set_rotation(45)
		i.set_color('r')
	#plt.plot_date(date,cl,'r^',label="Closing Curve")
	ax1.xaxis.label.set_color('b')
	ax1.yaxis.label.set_color('r')

	
	plt.xlabel("DATE")
	plt.ylabel("PRICE")
	plt.title("GOOGLE 10YRS")
	ax1.title.set_color('c')
	#ax1.set_yticks([0,50,75,100])
	ax1.legend()
	ax1.grid(True)
	print(time.clock()-t)
	plt.show()
		
	
get_data(goog_url)
