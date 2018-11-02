s='MCMXCIV'
listroman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']#单位
listinteger = [1000, 500, 100, 50, 10, 5, 1]
r_integer = 0
j = 0
for i in range(7):#从最高单位开始遍历
	if listroman[i] in s:
		k = 0
		k = s.count(listroman[i])
		r_integer += k * listinteger[i]#统计listroman[i]的个数并求和
		index_i = s.rfind(listroman[i])#定位最后一个listroman[i]的位置
		s = s.replace(listroman[i], 'Q')#将所有listroman[i]替换为‘Q’
		if i < 6:
			#m=0
			for m in range(index_i):#遍历最后一个listroman[i]前的字符
				q = 6 - i#listroman[i]后面的单位个数
				n = 0
				for n in range(q):
					j = 0
					if (i + 1 + n) < 7:#遍历listroman[i]后面的单位
						if s[m] == listroman[i + 1 + n]:
							j = j + 1#统计listroman[i + 1 + n]的个数
					r_integer -= j * listinteger[i + 1 + n]#减去listroman[i + 1 + n]的值
					s.replace(listroman[i+1+n],'Q',j)#替换掉listroman[i]前面的j个listroman[i + 1 + n]

		s = s[index_i:]#删除listroman[i]及其前面的数

print (r_integer)
