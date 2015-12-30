class Solution:
	# @param {string} s
	# @return {string}
	def shortestPalindrome(self, s):
		# A = s + s[::-1]
		A = s
		l = len(A)
		print A,l
		table = [0]*(l+1)
		i = 1
		cnt = 0
		pos = 2
		table[0] = -1
		while pos<l+1:
			if(A[pos-1] == A[cnt]):
				table[pos] = cnt+1
				cnt+=1
				pos+=1
			elif cnt>0:
				cnt = table[cnt]
			else:
				table[pos] = 0
				pos +=1
		print table
s = Solution()
print s.shortestPalindrome("abab")