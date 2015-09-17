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
		numstack = []
		maxstack = [] # the last digit is current max
		dnum = {}
		while i<l:
			num = nums[i]
			heapq.heappush(numstack,-num)
			if num not in dnum:
				dnum[num] =1
			else:
				dnum[num] +=1
			
			if i >= k:
				# print dnum,numstack
				dnum[nums[i-k]] -=1
				while dnum[-numstack[0]] == 0:
					heapq.heappop(numstack)
			maxstack.append(-numstack[0])
			i+=1
		return maxstack[k-1:]
s =Solution()
nums,k = [1,3,-1,-3,5,3,6,7],2
print s.maxSlidingWindow(nums,k)


