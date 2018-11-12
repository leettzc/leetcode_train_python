class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        sort_string = sorted(strs)
        result = ''
        for char in sort_string[0]: 
            if sort_string[-1].startswith(result+char):
                result +=char
            else:
                break
        return result