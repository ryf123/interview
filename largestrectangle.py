class Solution(object):
	def largestRectangleArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		l = len(height)
		if l == 0:
			return 0
		height = height +[0]
		# print height
		l = l+1
		i = 0
		stack = []
		maxarea = 0
		while i < l:
			# print i,height[i],stack
			if len(stack) == 0:
				stack.append(i)
				i+=1
			elif height[i] >= height[stack[-1]]:
				stack.append(i)
				i+=1
				# print stack
			else:
				p = stack.pop()
				h = height[p]
				w = i-stack[-1]-1 if len(stack) else i
				maxarea = max(maxarea,w*h)
		return maxarea
s = Solution()
height = [2,1,5,6,2,3]
print s.largestRectangleArea(height)

