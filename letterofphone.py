class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
    	ret = []
        for digit in digits:
        	print digit
        	letters = []
        	if digit == "2":
        		letters = ["a","b","c"]
        	if digit == "3":
        		letters = ["d","e","f"]
        	if digit == "4":
        		letters = ["g","h","i"]
        	if digit == "5":
        		letters = ["j","k","l"]
        	if digit == "6":
        		letters = ["m","n","o"]
        	if digit == "7":
        		letters = ["p","q","r","s"]
        	if digit == "8":
        		letters = ["t","u","v"]
        	if digit == "9":
        		letters = ["x","y","z"]
	        print ret		
	        array = []
	        for r in ret:
	        	for letter in letters:
	        		array.append(r+letter)
	        if len(ret) == 0:
	        	array = letters
	        if len(letters) > 0:
	        	ret = array
	return ret
s = Solution()
print s.letterCombinations("12345")
