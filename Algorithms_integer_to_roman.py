num = 1994
str=''
#listroman = ['M','IM','VM','XM','LM','CM','D','ID','VD','XD','LD','CD' ,'C','IC','VC','XC','L','IL','VL','XL','X','IX', 'V', 'IV', 'I']
#listinteger = [1000,999,995,990,950,900,500,499,495,490,450,400,100,99,95,90,50,49,45,40,10,9,5,4,1]
listroman = ['M','CM','D','CD' ,'C','XC','L','XL','X','IX', 'V', 'IV', 'I']
listinteger = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
for i in range(len(listinteger)):
	if num >=listinteger[i]:
		k = num//listinteger[i]
		num = num - k*listinteger[i]
		for j in range(k):
			str+=listroman[i]
print(str)