import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
from urllib import request
import numpy as np 
from datetime import datetime


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
	
	
	plt.plot_date(date,op,'-',label="Opening curve")
	#plt.plot_date(date,cl,'r^',label="Closing Curve")
	plt.xlabel("DATE")
	plt.ylabel("PRICE")
	plt.legend()
	plt.show()
		
	
get_data(goog_url)
