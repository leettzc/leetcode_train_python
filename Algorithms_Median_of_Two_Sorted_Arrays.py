nums1=[1,3]
nums2=[2,4]
nums=nums1+nums2
nums = sorted(nums)
if len(nums)%2==0:
	len_half = len(nums) // 2
	rnum = (nums[len_half-1]+nums[len_half])/2
else:
	len1_half = (len(nums)+1)//2
	rnum = nums[len1_half-1]
print(rnum)