#include "iostream"
#include "unordered_map"
#include "vector"
using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	unordered_map<int,int> d;
    	vector<int> ret;
    	for(int i=0;i<nums.size();++i){
    		int num = nums[i];
    		if (d.find(target-num) != d.end()){
    			ret.push_back(d[target-num]+1);
    			ret.push_back(i+1);
    			return ret;
    		}
    		if (d.find(num) == d.end()){
    			d[num] = i;
    		}
    	}
    	return ret;
        
    }
};
int main(int argc, char const *argv[])
{
	Solution s;
	vector<int> nums;
	nums.push_back(2);
	nums.push_back(3);
	nums.push_back(4);
	vector<int>ret = s.twoSum(nums,7);
	for(int num:ret){
		cout<<num<<endl;
	}
	return 0;
}