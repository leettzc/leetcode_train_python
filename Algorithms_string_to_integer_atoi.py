class Solution:
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		s_int = ''
		max = 2**31
		s = str.strip(' ')
		r_s = 0
		len_s = len(s)
		if s == '':
			return (0)
		if s[0] =='-':
			for i in s[1:]:
				if i.isdigit():
					s_int+=i
				else:
					len_s_int=len(s_int)
					j = 0
					for i in s_int:
						r_s =r_s + int(i)*(10**(len_s_int-1-j))
						j+=1
					if r_s > max :
						r_s = 0-(max)
						return r_s
					else:
						r_s = 0-r_s
						return r_s
			len_s_int=len(s_int)
			j = 0
			for i in s_int:
				r_s =r_s + int(i)*(10**(len_s_int-1-j))
				j+=1
			if r_s > max :
				r_s = 0-(max)
				return r_s
			else:
				r_s = 0-r_s
				return r_s
		if s[0] =='+':
			for i in s[1:]:
				if i.isdigit():
					s_int+=i
				else:
					len_s_int=len(s_int)
					j = 0
					for i in s_int:
						r_s =r_s + int(i)*(10**(len_s_int-1-j))
						j+=1
					if r_s >= max :
						r_s = max-1
						return r_s
					else:
						return r_s
			len_s_int=len(s_int)
			j = 0
			for i in s_int:
				r_s =r_s + int(i)*(10**(len_s_int-1-j))
				j+=1
			if r_s >= max :
				r_s = max-1
				return r_s
			else:
				return r_s
		if s[0].isdigit():
			for i in s:
				if i.isdigit():
					s_int+=i
				else:
					len_s_int=len(s_int)
					j =  0
					for i in s_int:
						r_s =r_s + int(i)*(10**(len_s_int-1-j))
						j+=1
					if r_s >= max:
						return (max-1)
					else:
						return r_s
			len_s_int=len(s_int)
			j = 0
			for i in s_int:
				r_s =r_s + int(i)*(10**(len_s_int-1-j))
				j+=1
			if r_s >= max :
				r_s = max-1
				return r_s
			else:
				return r_s
		else:
			return 0