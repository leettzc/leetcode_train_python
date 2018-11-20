class Solution:
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		q_list =[["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"], ["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
		r_str =[]
		if len(digits) == 0:
			return r_str
		if len(digits) == 1:
			return q_list[int(digits)-2]
		if len(digits) == 2:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					r_str.append(i+j)
			return r_str
		if len(digits) == 3:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					for k in q_list[int(list_digits[2])-2]:
						r_str.append(i+j+k)
			return r_str
		if len(digits) == 4:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					for k in q_list[int(list_digits[2])-2]:
						for l in q_list[int(list_digits[3])-2]:
							r_str.append(i+j+k+l)
			return r_str
		if len(digits) == 5:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					for k in q_list[int(list_digits[2])-2]:
						for l in q_list[int(list_digits[3])-2]:
							for m in q_list[int(list_digits[4])-2]:
								r_str.append(i+j+k+l+m)
			return r_str
		if len(digits) == 6:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					for k in q_list[int(list_digits[2])-2]:
						for l in q_list[int(list_digits[3])-2]:
							for m in q_list[int(list_digits[4])-2]:
								for n in q_list[int(list_digits[5])-2]:
									r_str.append(i+j+k+l+m+n)
			return r_str
		if len(digits) == 7:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					for k in q_list[int(list_digits[2])-2]:
						for l in q_list[int(list_digits[3])-2]:
							for m in q_list[int(list_digits[4])-2]:
								for n in q_list[int(list_digits[5])-2]:
									for p in q_list[int(list_digits[6])-2]:
										r_str.append(i+j+k+l+m+n+p)
			return r_str
		if len(digits) == 8:
			list_digits = []
			for str_digits in digits:
				list_digits.append(str_digits)
			for i in q_list[int(list_digits[0])-2]:
				for j in q_list[int(list_digits[1])-2]:
					for k in q_list[int(list_digits[2])-2]:
						for l in q_list[int(list_digits[3])-2]:
							for m in q_list[int(list_digits[4])-2]:
								for n in q_list[int(list_digits[5])-2]:
									for p in q_list[int(list_digits[6])-2]:
										for q in q_list[int(list_digits[7])-2]:
											r_str.append(i+j+k+l+m+n+p+q)
			return r_str
