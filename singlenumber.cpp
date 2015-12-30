#include "iostream"
#include "vector"
using namespace std;
class Solution {
public:
    int singleNumber(vector<int>& nums) {
    	int a = 0;
    	int b = 0;
		for(int c:nums){
			int ta = a;
			a = (a&~b&~c) | (~a&b&c);
			b = (~ta&b&~c) | (~ta&~b&c);
		}
		return a|b;   
    }
};
int main(int argc, char const *argv[])
{
	vector<int> nums;
	int array[] = {1,1,1,3,3,3,100};
	for(int a:array){
		nums.push_back(a);	
	}
	Solution s;
	cout<<s.singleNumber(nums)<<endl;
	return 0;
}
