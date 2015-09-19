class Solution:
	# @param {integer[]} height
	# @return {integer}
	def trap(self, height):
		l  = len(height)
		if l == 0:
			return 0
		# find left max value
		leftmax = 0
		rightmax = 0
		leftmaxes = []
		rightmaxes = []
		for i,h in enumerate(height):
			if h > leftmax:
				leftmax = h
			leftmaxes.append(leftmax)
		for i in range(1,l+1):
			if height[l-i] > rightmax:
				rightmax = height[l-i]
			rightmaxes.append(rightmax)
		total = 0
		print leftmaxes
		print rightmaxes
		for i in range(0,l):
			leftmax = leftmaxes[i]
			rightmax = rightmaxes[l-i-1]
			trap = (min(leftmax,rightmax) - height[i])
			if trap > 0:
				total += trap
		return total
s = Solution()
bars = [0,1,0,2,1,0,1,3,2,1,2,1]
print s.trap(bars)