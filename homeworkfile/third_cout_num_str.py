str1 = input("shu ru zi fu chuan: ")
countnum = 0
upcharacter = 0
lowercharacter = 0
num = 0
while num < len(str1):
	if str1[num].isupper():
		upcharacter = upcharacter + 1
	elif str1[num].islower():
		lowercharacter = lowercharacter + 1
	elif str1[num].isdigit():
		countnum = countnum + 1
	num = num + 1
print("总共有",len(str1),"个字符")
#print(countnum,upcharacter,lowercharacter)
'''	print("数字有，",coutnum,"个,大写字母有,",upcharacter,"个，小写字符有，"，lowercharacter,"个")
'''
print("数字有：",countnum)
print("大写字符有：",upcharacter)
print("小写字符有：",lowercharacter)
