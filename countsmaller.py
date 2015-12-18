# Given nums = [5, 2, 6, 1]
# Return the array [2, 1, 1, 0]
class Solution(object):
	def countSmaller(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		l = len(nums)
		i = l-1
		count = l*[0]
		while i>=0:
			num = nums[i]
			j = i+1
			while j<=l-1:
				if nums[j] < num:
					count[i] = count[j]+1
					break
				elif nums[j] == num:
					count[i] = count[j]
					break
				j+=1
			i-=1
		return count
s = Solution()
print s.countSmaller([5, 2, 6, 1])
print s.countSmaller([5])
print s.countSmaller([])
print s.countSmaller([1,2,3,4,5])
print s.countSmaller([5,4,3,2,1])