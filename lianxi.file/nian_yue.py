snian = eval(input("shu ru nian fen  >= 1990: "))
syue = eval(input("shu ru yue fen 1< yue < 12: "))
sday = eval(input("shu ru tian : "))
def pinrunn(snian):

	days = 0
	nsday = 0
	for i in range(1990,snian):
		if i % 4 == 0 and i % 100 != 0 or i % 400 ==0:
			nsday = 366
			days = days + nsday
		else :
			nsday = 365
			days = days + nsday
	return days
print(pinrunn(snian))
#xq = days % 7 
#print(xq)
'''
try:
except "异常名" as e:
		zhi xing ti 
else:
	不报错执行
finally:
	报错不报错都执行
'''






