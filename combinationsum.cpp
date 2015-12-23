#include "iostream"
#include "vector"
using namespace std;
class Solution {
public:
	vector<vector<int> > ret;
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
     	vector<int> path;   
        helper(candidates,target,0,path);
        return ret;
    }
    void helper(vector<int> nums,int target,int start,vector<int>& path){
		if(target == 0){
			ret.push_back(path);
			return;
		}
    	for (int i = start; i < nums.size() && target>=nums[i]; ++i)
    	{
    		int num = nums[i];
    		path.push_back(num);
    		helper(nums,target-num,i,path);
    		path.pop_back();
    	}
    }
};
int main(int argc, char const *argv[])
{
	int myints[] = {7,6,3,2};
  	vector<int> nums (myints, myints + sizeof(myints) / sizeof(int) );
  	Solution s;
  	for(vector<int> v:s.combinationSum(nums,7)){
  		for(int num:v){
  			cout<<num<<endl;
  		}
  	}
	return 0;
}