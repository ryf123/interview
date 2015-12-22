#include <iostream>
#include "vector"
using namespace std;
class Solution {
public:
    int missingNumber(vector<int>& nums) {
    	int total = 0;
    	int count = nums.size();
        for (int i = 0; i<count; ++i)
        {
        	total += nums[i];
        }
        return (0+count)*(count+1)/2 - total;
    }
};
int main()
{
	Solution s;
	int numsarray[] = {0,1,3};
	vector<int> nums (numsarray,numsarray+ sizeof(numsarray)/sizeof(int));
	int num = s.missingNumber(nums);
	cout<< num <<endl;

	return 0;
}
