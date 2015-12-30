#include "vector"
#include "assert.h"
#include "cmath"
#include "iostream"
using namespace std;
class Solution {
public:
    double myPow(double x, int n) {

    	long i = 1;
    	double total = x;
    	// vector<double> ret;
    	bool sign = true;
    	bool numsign = true;
    	if(total==0){
    		return 0;
    	}
    	if(x<0 && n%2!=0){
    		numsign = false;
    	}
    	if(n<0){
    		sign = false;
    		n = -n;
    		if(n==-2147483648){
    			n = 2147483647;
    		}
    	}
    	while(i<=n){
    		i *=2;
    		total*=total;
    	}
    	double power;
    	double current = total;
    	total = 1;
    	while(n){
    		i /=2;
    		current = sqrt(current);
    		if(i<=n){
    			total *= current;
    			n = n-i;    			
    		}
    	}
    	if(!numsign){
    		total = -total;
    	}
    	return sign?total:1/total;
    }
};
int main(int argc, char const *argv[])
{
	Solution s;
	cout<<s.myPow(-3,-3)<<endl;
	// cout<<s.myPow(1.0000,-2147483648)<<endl;
	// assert(s.myPow(2,10) == 1024);
	// assert(s.myPow(2,0) == 1);
	// assert(s.myPow(3,3) == 27);
	
	// cout<<s.myPow(3,-2)<<endl;
	return 0;
}