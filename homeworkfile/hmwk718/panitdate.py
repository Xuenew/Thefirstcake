import turtle
import datetime 
x=datetime.datetime.now().strftime("%Y%m%d")
print(x)
'''
shu ru shi jian bian li
'''
#def shuzi():

def huatu(k,data):
	turtle.speed(1)
	if data == "a":
		turtle.up()
		turtle.goto(k*20,0)
		turtle.down()
		turtle.goto(k*20+15,0)
	if data == "b":
		turtle.up()
		turtle.goto(k*20+15,0)
		turtle.down()
		turtle.goto(k*20+15,-15)
	if data == "c":
		turtle.up()
		turtle.goto(k*20+15,-15)
		turtle.down()
		turtle.goto(k*20+15,-30)
	if data == "d":
		turtle.up()
		turtle.goto(k*20+15,-30)
		turtle.down()
		turtle.goto(k*20,-30)
	if data == "e":
		turtle.up()
		turtle.goto(k*20,-30)
		turtle.down()
		turtle.goto(k*20,-15)
	if data == "f":
		turtle.up()
		turtle.goto(k*20,-15)
		turtle.down()
		turtle.goto(k*20,0)
	if data == "g":
		turtle.up()
		turtle.goto(k*20,-15)
		turtle.down()
		turtle.goto(k*20+15,-15)


def shu(zi):
	if zi =="0":
		ta = "abcdef"
	if zi =="1":
		ta = "bc"
	if zi =="2":
		ta = "abged"	
	if zi =="3":
		ta = "abgcd"	
	if zi =="4":
		ta = "fgbc"	
	if zi =="5":
		ta = "afgcd"	
	if zi =="6":
		ta = "afgacd"	
	if zi =="7":
		ta = "abc"	
	if zi =="8":
		ta = "abcdefg"	
	if zi =="9":
		ta = "abcfg"	
	return ta
'''
def main(x):
	for i in x:
		ta=shu(i)
		return ta
'''
for i in range(len(x)):
	shu(x[i])
	for j in shu(x[i]):
		huatu(i,j)
	
	
