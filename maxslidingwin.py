import heapq
class Solution(object):
	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		l,i = len(nums),0
		if l ==0:
			return []
		window = []
		maxstack = []
		for i,num in enumerate(nums):
			if window and window[0][0] <= i-k:
				window.pop(0)
			while window and window[-1][1] < num:
				window.pop() 
			window.append([i,num])
			maxstack.append(window[0][1])
		return maxstack[k-1:]
s =Solution()
nums,k = [1,3,-1,-3,5,3,6,7],5
print s.maxSlidingWindow(nums,k)


