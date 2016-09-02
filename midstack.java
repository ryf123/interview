import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */
class Node{
    int val;
    Node next=null;
    Node prev=null;
    public Node(int val){this.val =val;}
}
class MidStack
{
    Node dummyhead = new Node(1);
    Node dummytail = new Node(2);
    Node current = null;
    Node mid = dummyhead;
    int total = 0;
    public MidStack(){
        current = dummyhead;
        dummyhead.next = dummytail;
        dummytail.prev = dummyhead;
    }
    public Node getMid(){
        if(mid == dummyhead) return null; // if there is no mid
        return mid;
    }
    public void insert(int val){
        Node node = new Node(val);
        current.next.prev = node;
        node.prev = current;
        node.next = current.next;
        current.next = node;
        current = node;
        total++;
        if(total % 2 == 1){
            mid = mid.next;
        }
    }
    // return true if there is mid
    public boolean deletemid(){
        if(getMid() == null)
            return false;
        mid.prev.next = mid.next;
        mid.next.prev = mid.prev;
        mid = mid.prev;
        return true;
    } 
}
class Solution {
  public static void main(String[] args) {
    MidStack ms = new MidStack();
    for(int i=0;i<10;i++){
      ms.insert(i);
      System.out.println(ms.getMid().val);
    }
    
    ms.deletemid();
    System.out.println(ms.getMid().val);

  }
}