str1 = input("请输入一串字符串，并空格：")

'''
num = str1.count(' ')
time = 0
while time < (num + 1):
	print(str1.split(' ')[time][0].upper())
	time = time + 1
'''
'''
onestr = str1.split(' ')
num = len(onestr)
time = 0
while time < num:
	print(onestr[time][0].upper())
	time = time + 1
'''
i = 0
flag = True
while i < len(str1):
	if str1[i]=' ':
		flag = False
		print(str1[i.upper()],str1[i + 1].lower(),'asdf')
	i = i + 1














	
