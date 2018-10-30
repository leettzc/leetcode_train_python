s = "dvdf"
s1 = []
s2 = []
for i in s:
	if i not in s1:
		s1.append(i)
	else:
		print(s1)
		s2.append(len(s1))
		index1 = s1.index(i)
		s1 = s1[index1+1:]
		print(s1)
		s1.append(i)
print(s1)
s2.append(len(s1))
out = max(s2)
print(out)
