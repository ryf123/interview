#include "stack"
#include "iostream"
using namespace std;
class Queue {
public:
    stack<int> stack1;
    stack<int> stack2;
    int temp;
    void push(int x) {
        while(stack2.size()){
            temp = stack2.top();
            stack2.pop();
            stack1.push(temp);
        }
        stack1.push(x);
    }

    // Removes the element from in front of queue.
    void pop(void) {
        int temp;
        while(!stack1.empty()){
            temp = stack1.top();
            stack1.pop();
            stack2.push(temp);
        }
        if(!stack2.empty())
            stack2.pop();
    }

    // Get the front element.
    int peek(void) {
        int temp;
        while(!stack1.empty()){
            temp = stack1.top();
            stack1.pop();
            stack2.push(temp);
        }
        return stack2.top();
    }

    // Return whether the queue is empty.
    bool empty(void) {
        return stack1.empty() && stack2.empty();    }
};
int main(int argc, char const *argv[])
{
    /* code */
    Queue q;
    q.push(3);
    q.push(4);
    cout<<q.peek()<<endl;
    return 0;
}