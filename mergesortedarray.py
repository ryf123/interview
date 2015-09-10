class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		nums1[n:] = nums1[:m]
		# print nums1
		p1,p2 = n,0
		i = 0
		while i < m+n:
			print i,p1,p2
			if p1 == m+n:
				nums1[i] = nums2[p2]
				p2+=1
			elif p2 == n:
				nums1[i] =nums1[p1]
				p1+=1
			elif nums1[p1] <=nums2[p2]:
				nums1[i] =nums1[p1]
				p1+=1
			else:
				nums1[i] = nums2[p2]
				p2+=1
			i+=1
s = Solution()
nums1 = [1,3,5,0]
nums2 = [2]
s.merge(nums1,3,nums2,1)
print nums1
