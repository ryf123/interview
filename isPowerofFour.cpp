#include <iostream>
using namespace std;
class Solution {
public:
    bool isPowerOfFour(int num) {
    	int ones = 0;
        while(num != 0){
        	if(num == 1)
        		return true;
        	if((num & 1) != 0)
        		return false;
        	num >>= 1;
        	if((num & 1) != 0)
        		return false;
        	num >>= 1;
        }
        return false;
    }
};
int main(int argc, char const *argv[])
{
	Solution * s = new Solution();
	for (int i = 0; i < 17; ++i)
	{
		/* code */
		cout << i << ":" <<s->isPowerOfFour(i) << endl;
	}	
	return 0;
}
