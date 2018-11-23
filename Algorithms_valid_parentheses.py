class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
			if i in open_par:
				stack.append(i)#当i在open_par中时，添加到stack中
				print(stack)
			elif stack and i == bracket_map[stack[-1]]:#如果i等于i前一个字符在bracket_map中的键值
				stack.pop() #删除i前一个字符
			else:
				return False
		return stack == []

