
'''
for i in range(1,10):
	print("\t\n")
	for j in range(1,10):
		print("{}*{}={}".format(i,j-1,i*j,end=""))
	'''	
for i in range(1,10):
	print("")
	for j in range(1,i+1):
		print("{}*{}={}".format(j,i,i*(j)),end  = " ")
			
