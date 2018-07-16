import time
i = 0 
str1 = 20
while i <  str1:
	sr = i*"#"
	print("\r{}".format(sr),end='')
	i = i + 1
	time.sleep(0.5)
print()
