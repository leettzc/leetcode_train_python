nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
nums = sorted(nums)
r_nums = []
r_nums_1 = []
for i in range(0,len(nums)-2):
	for j in range(i+1,len(nums)-1):
		if nums[i]+nums[j] <= 0:
			k = 0-(nums[i]+nums[j])
			if k in nums[j+1:]:
				r_nums_1.append(nums[i])
				r_nums_1.append(nums[j])
				r_nums_1.append(k)
				if r_nums_1 not in r_nums:
					r_nums.append(r_nums_1)
				r_nums_1 = []
				k = 0
			else:
				k = 0
		else:
			print(r_nums)
print(r_nums)


