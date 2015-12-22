from collections import Counter
import sys
class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		worddict = Counter()
		lt = len(t)
		for tt in t:
			worddict[tt]+=1
		redundantdict = Counter()
		windowstack = []
		minWindowlen = sys.maxint
		left,right = 0,0
		noredundantlen = 0
		redundantcount = 0
		for i,letter in enumerate(s):
			if letter in worddict:	
				windowstack.append([letter,i])
				if worddict[letter] == 0:
					redundantdict[letter] +=1
					redundantcount +=1
				else:
					worddict[letter] -=1
					noredundantlen +=1
				if noredundantlen ==lt:
					while len(windowstack) and redundantdict[windowstack[0][0]] > 0:
						prevleft = windowstack.pop(0)
						redundantdict[prevleft[0]] -=1
						redundantcount-=1
					if windowstack[-1][1] - windowstack[0][1] + 1 < minWindowlen: left,right = windowstack[0][1],windowstack[-1][1] minWindowlen = windowstack[-1][1] - windowstack[0][1] + 1 # print windowstack
		if noredundantlen !=lt:
			return ""
		if windowstack[-1][1] - windowstack[0][1] + 1 < minWindowlen:
			left,right = windowstack[0][1],windowstack[-1][1]
		return s[left:right+1]
sl = Solution()
s = "bba"
t = "ab"
s = "baba"
t = "abb"
print sl.minWindow(s,t)