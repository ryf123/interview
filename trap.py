class Solution:
	# @param {integer[]} height
	# @return {integer}
	def trap(self, height):
		l  = len(height)
		if l <= 2:
			return 0
		leftmax = [0] * l
		rightmax = [0] * l
		maxnum = height[0]
		i = 1
		while i<l:
			maxnum= max(maxnum,height[i])
			leftmax[i] = maxnum
			i+=1
		i = l-2
		maxnum = height[l-1]
		while i>=0:
			maxnum = max(maxnum,height[i])
			rightmax[i] = maxnum
			i-=1
		trap = 0
		# print leftmax
		# print rightmax
		# print height
		for i in range(1,l-1):
			trap += (min(leftmax[i],rightmax[i]) - height[i])
		return trap
s = Solution()
bars = [0,1,0,2,1,0,1,3,2,1,2,1]
bars = [2,0,2]
print s.trap(bars)