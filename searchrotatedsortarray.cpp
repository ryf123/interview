#include "vector"
#include "iostream"
using namespace std;
class Solution {
public:
    int search(vector<int>& nums, int target) {
 		int start = 0;
 		int end = nums.size() - 1;
 		int mid;
 		while(start<=end){ 
 			mid = (start+end)/2;
 			if(target == nums[mid]){
 				return mid;
 			}
 			//if first half is sorted
 			if(nums[start]<=nums[mid]){ 
 				if(target>=nums[start] && target<=nums[mid]){
 					end = mid-1;
 				}
 				else{
 					start = mid+1;
 				}
 			}
 			//second halp is sorted
 			else{
 				if(target>=nums[mid] && target<=nums[end]){
 					start = mid+1;
 				}
 				else{
 					end = mid-1;
 				} 				
 			}
 		}
 		return -1;       
    }
};
int main(int argc, char const *argv[])
{
	vector<int> nums;
	// nums.push_back(2);
	// nums.push_back(3);
	// nums.push_back(4);
	nums.push_back(1);
	Solution s;
	cout<<s.search(nums,1)<<endl;;
	return 0;
}