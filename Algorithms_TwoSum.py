def twoSum( nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	arr = []
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i != j:
				sum = nums[i] + nums[j]
				if sum == target:
					arr.append(i)
					arr.append(j)
					return arr
	return('no solution')
