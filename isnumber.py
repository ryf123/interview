# Sep 13 9:30--10:00
# the only letter valid is e
# it can be e+digit or e-digit or edigit
# decimal point can't be after e
class Solution(object):
	def isNumber(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		l = len(s)
		start,end = 0,l-1
		while start<end:
			if s[start] == " ":
				start+=1
			else:
				break
		while start<end:
			if s[end] == " ":
				end -=1
			else:
				break
		if start > end:
			return False
		if s[start] == "+" or s[start] == "-":
			start+=1
		if start > end:
			return False
		e,sign,digit,decimal = False,False,False,False
		for i in range(start,end+1):
			if s[i].isdigit():
				digit = True
			elif s[i] == "e":
				if e or sign or not digit:
					return False
				if i==end:
					return False
				e = True
			elif s[i] == "+" or s[i] == "-":
				if not (i-1 >= start and s[i-1] == "e"):
					return False
				if i==end:
					return False
				sign = True
			elif s[i] == ".":
				if e or decimal:
					return False
				if i==end and not digit:
					return False
				decimal = True
			else:
				return False
		return True

tests = ["0","2e10","1 a"," 0.1 ","01","0.1e123","123e+123","1e0.1","e9",". 1","-1.",".",".1",".+","0e","3.","4e+","e+1"]
s = Solution()
for t in tests:
	print t,s.isNumber(t)

# expected result
# 0 True
# 2e10 True
# 1 a False
#  0.1  True
# 01 True
# 0.1e123 True
# 123e+123 True
# 1e0.1 False
# e9 False
# . 1 False
# -1. True
# . False
# .1 True
# .+ False
# 0e False
# 3. True
# 4e+ False
# e+1 False