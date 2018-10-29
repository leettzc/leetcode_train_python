class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		str1 = x
		str = 0
		y = 0
		if x < 0:
			return (1 == 0)
		if 0 <= x < 10:
			return (1 == 1)
		while x >= 10:
			y = x % 10
			x = x // 10
			str = str * 10 + y * 10
		str = str + x
		if str1 == str:
			return (1 == 1)
		else:
			return (1 == 0)
