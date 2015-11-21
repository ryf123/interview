class Solution:
	# @param {string} s
	# @return {string}
	def longestPalindrome(self, s):
		l =  len(s)
		if l ==0:
			return s
		maxlen = 0
		start = 0
		end = 0
		if s == s[::-1]:
			return s
		for i in range(l-1,-1,-1):
			for j in range(1,l):
				if i-j>=0 and i+j<l:
					if s[i-j] == s[i+j]:
						if 2*j+1 > maxlen:
							maxlen = 2*j+1
							start,end = i-j,i+j
							# print i,j,maxlen
					else:
						break
			for j in range(1,l):
				if i-j+1 >= 0 and i+j <l:
					if s[i-j+1] == s[i+j]:
						if 2*j > maxlen:
							maxlen = 2*j
							start,end = i-j+1,i+j
					else:
						break
		return s[start:end+1]
s = Solution()
st = "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
print s.longestPalindrome(st)