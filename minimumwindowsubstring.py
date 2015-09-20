class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		d = {}
		lt = len(t)
		for tt in t:
			if tt not in d:
				d[tt] = 1
			else:
				d[tt] = d[tt]+1
		left = 0
		windowlengh = None
		count = 0
		stack = []
		# print d
		for i,ss in enumerate(s):
			if ss in d:
				if d[ss] >0:
					d[ss] -=1
					count +=1
				elif d[ss] == 0:
					stack.append(ss)
			if count == lt:
				if s[left] not in d:
					left +=1
				if ss == s[left] or not windowlengh:
					if windowlengh:
						left +=1
						stack.pop()
					while (left < i and s[left] not in d) or len(stack)>0:
						if s[left] not in d:
							left +=1
						if len(stack) >0:
							match = False
							for k,st in enumerate(stack):
								if s[left] == st:
									stack.pop(k)
									left +=1
									match = True
							if not match:
								break
				if not windowlengh:
					windowlengh = s[left:i+1]
				elif i-left < len(windowlengh):
					windowlengh = s[left:i+1]
			# print windowlengh,count

		# print count
		return windowlengh if count == lt else ""
sl = Solution()
s = "a"
t = "abc"
print sl.minWindow(t,s)