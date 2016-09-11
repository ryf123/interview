//Given a list of nodes, each with a left child and a 
//right child (they can be null), determine if all 
//nodes belong in a single valid binary tree. The root is not given.
boolean single_valid_tree(List<Node> nodes){
	HashMap<Node,Node> parent = new HashMap();
	for(Node node:nodes){
		if(node == null)
			continue;
		if(node.left != null){
			if(parent.containsKey(node.left)) // if node.left already has a parent, then it's invalid
				return false;
			parent.put(node.left,node);
		}
		if(node.right != null){
			if(parent.containsKey(node.right)) // same for node.right
				return false;
			parent.put(node.right,node);
		}
		Node root = null; // root does not have a parent
		for(Node node:nodes){
			if(!parent.containsKey(node)){
				if(root != null) // if there is already a root
					return false;
				root = node;
			}
		}
		if(root == null)
			return false;
		int count = 0;
		// there might be a cycle e.g node1.left = node2; node2.left = node1;
		// we should be able to traverse all node from the root
		Queue<Node> queue = new LinkeList();
		queue.offer(root);
		HashSet<Node> visited = new HashSet();
		while(queue.size() > 0){
			Node node  = queue.poll();
			count++;
			if(visited.contains(node)) // cycle
				return false;
			visited.add(node);
			if(node.left != null)
				queue.offer(node.left);
			if(node.right != null)
				queue.offer(node.right);
		}
		return count == parent.size() + 1;

	}
}