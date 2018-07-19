'''
intx = eval(input("shu ru yi ge shu qiu fang :"))
def intfang(intx):
	x = 0
	x = intx**2
	return x
fang = intfang(intx)
print(fang)
'''
'''
def numall(n,*arg):
	s = n
	for i in arg:
		s = s + i
	print(s)
	return s
print(numall(1,23,4,5))
'''
'''
print("sd")
for i in range(1,10,-1):
	print("i")
	for j in range(i-1,1):
		print("sd")
		print("{}*{}={}".format(j,i,i*j),end=' ')
'''
for i in range(10,-1,-1):
	print(i)
	for j in range(i-1,1):
		print("{}*{}={}".format(j,i,i*j,end=" "))
