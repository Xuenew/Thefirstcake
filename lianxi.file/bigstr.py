str1 = input("shu ru yi ge zhi fu chuang :")
lon = len(str1)
for i in str1:
	m = str1[0]
	if i > m :
		m = i
print(m)
k = 0
for i in range(lon+1):
	if ord(str1[i])<ord(str1[i+1]):
		k = i
print(str1[k])
		
