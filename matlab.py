import matplotlib.pyplot as plt 

def details(name,day_act,marks):
	act=["Physics","Digital","EM-Theory"]
	cols=['r','b','c']
	plt.subplot(211)
	
	plt.title(name+"Marks")
	plt.pie(marks,labels=act,colors=cols,shadow=True,startangle=90,autopct="%1.1f%%")

	act=["Sleeping","Playing","Working"]
	plt.subplot(212)
	plt.title(name+"Activities")
	plt.pie(day_act,labels=act,colors=cols,shadow=True,startangle=90,autopct='%1.1f%%')

	plt.show()


name=input("Enter thy name")
day_act=list(map(int,input("Enter the hours of Sleeping Playing nd Working").strip().split()))
marks=list(map(int,input("Enter marks in Phy Dig nd EM").strip().split()))
details(name,day_act,marks)
