from collections import Counter
import sys
class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		d = {}
		worddict = Counter()
		lt = len(t)
		for tt in t:
			worddict[tt]+=1
			d[tt] = True
		minWindowlen = sys.maxint
		minindex = None
		left,right = 0,-1
		count = len(t)
		while right < len(s) and left<len(s):
			if count:
				right+=1
				if right >= len(s):
					continue
				letter  = s[right]
				if letter in d:
					worddict[letter] -=1
					if worddict[letter] >= 0:
						count-=1
			else:
				if left>=len(s):
					continue
				if right-left <minWindowlen:
					minWindowlen = right-left
					minindex = left
				letter = s[left]
				if letter in d:
					worddict[letter] +=1
					if worddict[letter] >0:
						count +=1
				left+=1
		if minindex == None:
			return ""
		return s[minindex:minindex+minWindowlen+1]


				
sl = Solution()
s = "bba"
t = "ab"
s = "baba"
t = "abb"
s ="ADOBECODEBANC"
t = "ABC"
print sl.minWindow(s,t)