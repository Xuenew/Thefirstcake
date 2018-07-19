ser = eval(input("shu ru ni de sheng gao /m: "))
tiz = eval(input("shu ru ni de ti zhong /kg: "))
bim = (tiz/ser)**2
if 18.5 < bim < 23.9:
	print("zheng chang ")
if 24 < bim < 27:
	print("guo zhong ")
if 28 < bim < 32:
	print("fei pang ")
if bim > 32:
	print("fei chang fei pang")

