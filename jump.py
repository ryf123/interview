class Solution:
	# @param {integer[]} nums
	# @return {boolean}
	def jump(self, nums):
		# the maximum it can jump is current max(nums[i],canJump[i-1])
		l = len(nums) 

		start,end = 0,0
		sol = 0
		while end < l-1:

			maxjump = end
			# print start,end
			for x in range(start,end+1):
				# print nums[x],x,start,end
				if nums[x]+x > maxjump:
					# sol +=1
					maxjump = nums[x]+x
					start,end = x,nums[x]+x

			if maxjump != 0:
				sol+=1
			else:
				break
		return sol


s = Solution()
jumps = [2,3,1,4]
test = [3,1,1,3,1,1,3,1,1,1]

tests = [[0]]
tests.append(jumps)
tests.append(test)
tests.append([6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3])
tests.append([5,9,3,2,1,0,2,3,3,1,0,0])
# print len(jumps)
for t in tests:
	print t,s.jump(t)
