class System{
  TreeMap<Long,Integer> time_map = new TreeMap();
  TreeMap<Integer,HashSet<Long>> value_map = new TreeMap();
  int getMax() throws Exception{
    if(value_map.size() == 0)
      throw new Exception();
    return value_map.lastKey();
  }
  int getMin() throws Exception{
    if(value_map.size() == 0)
      throw new Exception();
    return value_map.firstKey();
  }
  int getRecent() throws Exception{
    if(time_map.size() == 0)
      throw new Exception();
    return value_map.lastKey();
  }

  void add(long time, int price){
    time_map.put(time,price);
    if(!value_map.containsKey(price))
      value_map.put(price,new HashSet<Long>());
    value_map.get(price).add(time);
  }
  void update(long time, int price) throws Exception{
    remove(time); // remove old value
    add(time,price); // add new value
  }
  void remove(long time) throws Exception{
    if(!time_map.containsKey(time))
      throw new Exception();
    int value = time_map.get(time);
    time_map.remove(time);
    value_map.get(value).remove(time);
    if(value_map.get(value).size() == 0)// remove the set if empty
      value_map.remove(value);
  }
  public static void main(String[] args) {
    System s = new System();
    try{
      s.add(1,10);
      s.add(2,100);
      System.out.println(s.getMax());
      System.out.println(s.getMin());
      s.update(1,1000);
      System.out.println(s.getMax());
      System.out.println(s.getMin());
      s.remove(1);
      System.out.println(s.getMax());
      System.out.println(s.getMin());
    }
    catch(Exception e){
    }
    finally{
    }
  }
}