def findintervalmax(nums):
	l = len(nums)
	if l == 0:
		return 0
	prev = nums[0]
	_prev = 0
	i = 1
	while i<l:
		current = max(prev,nums[i]+_prev)
		_prev = prev
		prev = current
		i+=1
	return prev
assert(findintervalmax([4,9,6])==10)
assert(findintervalmax([4,10,3,1,5])==15)