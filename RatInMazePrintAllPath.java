package oops;

public class RatInMazePrintAllPath {

	

	public static boolean ratInMaze(int maze[][]) {
		int n=maze.length;
		int path[][]=new int[n][n];
		return ratInMaze(maze,path,0,0);
		
	}
	public static boolean ratInMaze(int maze[][],int path[][],int i,int j) {
		int n=maze.length;
		// Maze index should not be out of bound
		if(i<0 || j<0 || i>=n || j>=n || maze[i][j]==0 || path[i][j]==1) {
			return false;
		}
		path[i][j]=1;
		// Now check the condition in all direction
		// Destination condition
		if(i==n-1 && j==n-1) {
			for(int l=0;l<n;l++) {
				for(int m=0;m<n;m++) {
					if(path[l][m]!=0)
					{
					System.out.print(path[l][m]);
					}
					else {
					System.out.print(' ');
					}
				}
				System.out.println();
			}
			return true;
		}
		// At Top
		
		if(ratInMaze(maze,path,i-1,j)) {
//			path[i][j]=1;
			return true;
		}
		
		// At Bottom
		
		if(ratInMaze(maze,path,i+1,j)) {
//			path[i][j]=1;
			return true;
			
		}
		//At Left
		if(ratInMaze(maze,path,i,j-1)){
//			path[i][j]=1;
			return true;
		}
		// At RIght
		if(ratInMaze(maze,path,i,j+1)){
//			path[i][j]=1;
			return true;
		}
		
		
		return false;
		
		
		
		
		
	}
	
	
	public static void main(String[] args) {
		int maze[][]= {{1,1,1},{0,1,0},{1,1,1}};
		boolean p=ratInMaze(maze);
		System.out.print(p);
		

	}



}
