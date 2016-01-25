/*
 * Definition for singly-linked list.
*/
#include "vector"
#include "queue"
#include "iostream"
using namespace std;
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    	int length1 = 0;
    	int length2 = 0;
    	ListNode* current1 = l1;
    	ListNode* current2 = l2;
    	while(current1){
    		current1 = current1->next;
    		length1++;
    	}
    	while(current2){
    		current2 = current2->next;
    		length2++;
    	}
    	ListNode* dummyhead = new ListNode(1);
    	int addon = dfs(dummyhead,l1,l2,length1,length2);
    	return addon?dummyhead:dummyhead->next;
    }
private:
	int dfs(ListNode* head,ListNode* n1,ListNode* n2,int l1,int l2){
		if(!n1 && !n2){
			return 0;
		}
		ListNode* next = new ListNode(1);
		if(l1>l2){
			next->val = (n1->val)+dfs(next,n1->next,n2,l1-1,l2);
		}
		else if(l2>l1){			
			next->val = (n2->val)+dfs(next,n1,n2->next,l1,l2-1);
			
		}
		else{
			next->val = (n2->val)+(n1->val)+dfs(next,n1->next,n2->next,l1-1,l2-1);
		}
		int addon = (next->val)/10;
		next->val = (next->val)%10;
		head->next = next;
		return addon;
	}
};
int main(int argc, char const *argv[])
{
	Solution s;
	ListNode* head1 = new ListNode(9);
	head1->next = new ListNode(9);
	ListNode* head2 = new ListNode(0);
	// head2->next = new ListNode(1);
	ListNode* newhead = s.addTwoNumbers(head1,head2);
	while(newhead){
		cout<<newhead->val<<endl;
		newhead = newhead->next;
	}
	return 0;
}