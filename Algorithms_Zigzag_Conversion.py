s="ABCD"
r_s=""
numRows = 2
len_s = len(s)
if numRows == 1:
	print(s)
if numRows > len_s:
	print(s)
numColumns = (len_s//(numRows+numRows-2)+1)*(numRows-1)
N = [([0] * numColumns) for nn in range(numRows)]
i = 0
j = 0
m = 0
n = len_s +1
for s_value in s:
	if m == numRows:
		n = 0
		i -= 1
		m = len_s +1
	if n == numRows-2:
		m = 0
		i = 0
		j+=1
		n = len_s +1
	if m < numRows:
		N[i][j] = s_value
		i+=1
		m+=1
	if n < numRows-2:
		i-=1
		j+=1
		N[i][j] = s_value
		n+=1
for x in range(numRows):
	for y in range(numColumns):
		if N[x][y]!=0:
			r_s+=N[x][y]
print(N)
print(r_s)


