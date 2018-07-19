import random
num = eval(input("shu ru yi ge shu zi: "))
time = True

for i in range(3):
	g = random.randint(1,10)
	if num == g:
		print(" gong xi ni ni da dui l !!")
	elif num > g:
		print("ni de shu da l zai ge ni yi ci ji hui!!")
		num = eval(input("shu ru yi ge shu zi: "))
		time = False
	else:
		print("da dan yi dian!!")
		time = False
		num = eval(input("shu ru yi ge shu zi: "))
if time !=True:
	print("yong hu ui duo san ci ji hui !!")

