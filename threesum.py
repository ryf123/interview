class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def twoSum(nums, target):
			l = len(nums)
			if not l:
				return []
			high = l - 1
			low = 0
			ret = []
			while(low < high):
				if nums[high] + nums[low] == target:
					ret.append([nums[low],nums[high]])
					high -=1
					low +=1
					if high != l-1:
						while(high > low and nums[high]==nums[high+1]):
							high-=1
					if low != 0:
						while (high > low and nums[low] == nums[low-1]):
							low +=1
				elif nums[high] + nums[low] > target:
					high -=1
				else:
					low+=1
			return ret
		nums.sort()
		l = len(nums)
		ret = []
		d = {}
		for i,num in enumerate(nums):
			if i>0:
				if nums[i] == nums[i-1]:
					continue
			minus = 0-num
			sum2 = twoSum(nums[i+1:],minus)
			if sum2:
				for r in sum2:
					ret.append([num]+r)
				
		return ret
s = Solution()
#nums = [1,2,-1,0]
#nums =  [12,5,-12,4,-11,11,2,7,2,-5,-14,-3,-3,3,2,-10,9,-15,2,14,-3,-15,-3,-14,-1,-7,11,-4,-11,12,-15,-14,2,10,-2,-1,6,7,13,-15,-13,6,-10,-9,-14,7,-12,3,-1,5,2,11,6,14,12,-10,14,0,-7,11,-10,-7,4,-1,-12,-13,13,1,9,3,1,3,-5,6,9,-4,-2,5,14,12,-5,-6,1,8,-15,-10,5,-15,-2,5,3,3,13,-8,-13,8,-5,8,-6,11,-12,3,0,-2,-6,-14,2,0,6,1,-11,9,2,-3,-6,3,3,-15,-5,-14,5,13,-4,-4,-10,-10,11]
nums = [11,2,-10,12,-10,11,9,4,2,-9,-12,-4,0,8,-6,-5,8,5,-15,-14,-1,14,-6,-12,3,-5,7,-3,9,-8,-3,-3,2,-6,-14,7,12,11,-4,-9,-13,-1,3,2,-8,12,4,7,-6,-4,1,8,-5,10,12,13,12,4,-13,-2,4,-9,10,-9,-8,4,5,-11,0,-13,-12,-6,-7,6,11,-7,-5,-8,-15,4,3,1,-11,13,-12,8,3,8,-10,5,-9,9,11,9,7,10,-2,-3,14,13]
#nums = nums + nums +nums + nums
nums  = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print s.threeSum(nums)
# print len(s.threeSum(nums))