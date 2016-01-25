class Solution:
	# @param {string} s
	# @return {string}
	def shortestPalindrome(self, s):
		A = s + s[::-1]
		cnt = [0]
		l = len(A)
		for i in range(1,l):
			index = cnt[i-1]
			while(index >0):
				if (A[index] == A[i]):
					if index < len(s):
						break
				# else:
				index =cnt[index-1]
			cnt.append(index + 1 if A[index] ==A[i] else 0)
		prefixl =  cnt[-1]
		return s[prefixl:][::-1]+s
s = Solution()
print s.shortestPalindrome("aabba")
