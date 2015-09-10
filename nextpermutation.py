class Solution:
	# @param {integer[]} nums
	# @return {void} Do not return anything, modify nums in-place instead.
	def nextPermutation(self, nums):
		# e.g. 123
		l = len(nums) # l= 3
		i = 0
		while i < l: # i in range 0,1,2
			appendarray = [] 
			num = nums[l-i-1] # num = nums[2] nums[1] nums[0]
			if(l-i-1-1 >= 0): # if it has previous value if num[n] > num[n-1] swap with the minimum in num[n:l] that is larger than num[n-1]
				prevnum = nums[l-i-1-1] #nums[1] in 1st iter 2
				currentnums = nums[l-i-1:l] # [3]
				maxnum = max(currentnums)
				if(maxnum > prevnum):
					array = []
					for minmaxnum in currentnums:
						if minmaxnum > prevnum:
							array.append(minmaxnum)
					minmaxnum = min(array) # find the min value of the values which are greater than pre value
					index = nums[l-i-1:l].index(minmaxnum) 

					nums[l-i-1-1] = minmaxnum # swap

					nums[l-i-1+index] = prevnum

					nums[l-i-1:l] =  sorted(nums[l-i-1:l])
					print nums
					break
			i+=1
		if(i == l):
		 	nums.sort()
		return nums
s = Solution()
print s.nextPermutation([1,2])