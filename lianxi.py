week = "星期一星期二星期三星期四星期五星期六星期日"
userinput = input("请输入1～7之间任意数字")
'''1-2 2-5 3-8 4-11 n+2n-1'''
x = int(userinput)
#a = x+2*x-1-2
#b = x+2*x
print("今天是:",week[x+2*x-3:x+2*x])
#print(a)
