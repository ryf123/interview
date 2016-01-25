#include <iostream>
#include "unordered_map"
#include "list"
using namespace std;
class LRUCache{
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        auto i = cache.find(key);
        if(i!= cache.end()){
        	move_to_head(key);
        	return i->second.first;
        }
        else{
        	return -1;
        }
    }
    
    void set(int key, int value) {
        auto i  = cache.find(key);
        if(i!= cache.end()){
        	i->second.first = value;
        	move_to_head(key);
        }
        else{
        	if(cache.size()==capacity){
        		cache.erase(l.back());
        		l.pop_back();
        	}
    		l.push_front(key);
    		cache[key] = {value,l.begin()};
        }

    }
    void move_to_head(int key){
    	l.erase(cache[key].second);
    	l.push_front(key);
    	cache[key].second = l.begin();
    }
private:
	int capacity;
	unordered_map<int,pair<int,list<int>::iterator> > cache;
	list<int> l;
};