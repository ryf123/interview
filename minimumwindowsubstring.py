class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		d = {}
		# count each letter occurence in t
		for c in t:
			if c not in d:
				d[c] = 1
			else:
				d[c] += 1
		l = len(t)
		ls = len(s)
		start = 0
		ret = s
		ret_start,ret_end = 0,ls-1
		ret = False
		for i,c in enumerate(s):
			if c in d: # if this letter is in t
				d[c] -= 1
				if d[c] >= 0: # if this letter is 'effective' letter, in the end l should be 0
					l -= 1
					while l == 0 and start < ls:
						if ret_end - ret_start  >= i - start:
							ret_start,ret_end = start,i
							ret = True
						if s[start] in d:
							d[s[start]] += 1
							if d[s[start]] > 0:
								l += 1
						start += 1
		return s[ret_start:ret_end+1] if ret else ""





				
sl = Solution()
s = "a"
t = "a"
s = "baba"
t = "abb"
s ="ADOBECODEBANC"
t = "ABC"
print sl.minWindow(s,t)