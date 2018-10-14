
  public LCA(Digraph g){
		this.graph = g;
	}

	public boolean hasCycle(){
		DirectedCycle testDAG = new DirectedCycle(graph);
		return testDAG.hasCycle();
	}


	public int lowestCommonAncestor(int a, int b){
		if(hasCycle()){
			return -1;
		}else if(graph.V()==0){
			return -1;
		}else{

			DirectedDFS DFS_A = new DirectedDFS(graph, a);
			DirectedDFS DFS_B = new DirectedDFS(graph, b);
			boolean[]am = DFS_A.marked;
			boolean[]bm = DFS_B.marked;
			for(int i = 0; i<am.length; i++){
				if(am[i]==bm[i]){
					return i;
				}
			}
			return -1;
		}
	}

	public static void main(String[]args){
		Digraph v = new Digraph(0);
		v.addEdge(0, 1);
	}
