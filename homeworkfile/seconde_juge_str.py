str1 = input("输入第一条字符串: ")
str2 = input("输入第二条字符串: ")
str1len = len(str1)
str2len = len(str2)
num = 0
while num < len(str1):
	if ord(str1[num]) < ord( str2[num]):
		print("字符串二的,",str2[num],"大于第一条字符串的,",str1[num])
		break			
	if ord(str1[num]) >  ord(str2[num]):
		print("字符串一的,",str1[num],"大于第二条字符串的,",str2[num])
		break
	if ord(str1[num]) == ord(str2[num]):
		num = num + 1
	
	
		
	
