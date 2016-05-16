#include <iostream>
#include "vector"
#include <assert.h>
using namespace std;

class Solution {
public:
	
    bool isValidSerialization(string preorder) {
    	vector<int> v;
		if(preorder[0] == '#'){
			if(preorder.size() == 1)
    			return true;
    		else
    			return false;
		}
        for (int i = 0; i < preorder.size();)
        {
        	// printf("i:%d\n",i );
        	if (v.size() == 0 && i >0)
    		{
    			return false;
    		}
        	if(preorder[i] == '#'){

        		while(v.back() == 1){
        			v.pop_back();
        		}
        		if(v.size() > 0 && v.back() == 2){
        			v[v.size()-1] = 1;
        		}

        	}
        	else if (preorder[i] == ',')
        	{
        	}
        	else{
        		while(i+1 < preorder.size() && isdigit(preorder[i+1])){
        			i++;
        		}
        		v.push_back(2);
        	}
        	i++;
	        // for(int _:v){
        	// 	printf("%d,",_);
        	// }
        	// printf("\n");
        }
        return v.size() == 0;
    }
};
int main()
{
	Solution * s = new Solution();
	cout<<s->isValidSerialization("99,#,#")<<endl;
	cout<<s->isValidSerialization("9,#,#,1")<<endl;
	assert(s->isValidSerialization("9,3,4,#,#,1,#,#,#,2,#,6,#,#") == 0);
	assert(s->isValidSerialization("#,#,#") == 0);
	assert(s->isValidSerialization("9,312312312312,4333,#,#,1,#,#,2,#,6,#,#") == 1);
	return 0;
}