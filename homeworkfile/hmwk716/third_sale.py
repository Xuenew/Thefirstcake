buy = eval(input("shu ru ni mai de price:"))
x = 0
if 50<=buy<=100:
	x =(buy*0.9)
	print("{},de zhe ko finally price is {}".format(10,x))
if buy >100:
	x = (buy*0.8)
	print("{},de zhe ko finally price is {}".format(20,x))

