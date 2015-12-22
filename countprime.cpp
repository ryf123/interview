#include "iostream"
#include "math.h"
#include "vector"
#include "assert.h"
using namespace std;
class Solution {
public:
    int countPrimes(int n) {
    	// bool prime[n] = {0};
    	vector<bool> prime(n, true);
    	int total=0;
    	double root = sqrt(n);
    	for (int i = 2; i < n; ++i)
    	{
    		if (prime[i] == true){
    			total +=1;
    			if (i > root)
    				continue;
    			for (int j = i*i; j < n; j+=i)
    			{
    				prime[j] = false;
    			}
			}
    	}
    	return total;
    }
};
int main()	
{
	Solution s;
	cout<<s.countPrimes(10)<<endl;
	assert(s.countPrimes(10) == 4);
	return 0;
}