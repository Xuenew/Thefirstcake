shu = input("shu ru yi ge shu :")
'''
long1 = len(shu)
shifo =  1
for i in range(long1-1):
	if shu[i]!= shu[i+1]:
		shifo = 0
#print("{}{}shi hui wen zheng xing".format("shi" if  shifo = True else "bu shi"))
if shifo ==  1 :
	print("shi hi wen shu")
else:
	print("bu shi hui wen zhi shu")
'''
'''
print(shifo)
'''
# 456
save =int( shu) # bao cun shu ju 
rang = len(shu)# chang du
save1 = int(shu)
k = 0
l = ""
for i in range(rang):
	num = save % 10
	k = num
	save = save // 10
	#print(str(k))
	#l = str(k)+l
	#print(l)
x = save1 % 10
print(k,x,"\n")
if k == x:
	print("shi hui wen shu ")
else:
	print("bu shi hui wen shu")
'''
print(save%10)
if k == (save%10):
	print("shi hui wen")
else:
	print("bu shi hui wen")
'''
