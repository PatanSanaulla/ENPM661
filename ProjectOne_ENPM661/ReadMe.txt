ENPM661

Project One - 8 Puzzle Problem

Code uses the following packages, 
numpy - for converting the 2D matrix to 1D
copy - for deep copy of the tile values to generate moves
sys - for reading the input as an argument, and exiting the code in case or error scenarios

Consider a sample 8 puzzle with values which is to be solved,
1 0 3 
4 2 5 
7 8 6 
Note: The code accepts the node entry in column wise manner, i.e "1 4 7 0 2 8 3 5 6" in a string format with spaces.
- To run the code:
   >> python 8PuzzleSolver.py "1 4 7 0 2 8 3 5 6"

- Output: The output are 3 files
  NOTE: The nodes are printed in column wise manner.

  ** If the input is in incorrect format, or the given values are unsolvable then the output is printed on the terminal
  Also in the file that it is unsolvable cube values.

  1. "Nodes.txt"
  Each Node generated in the tree is shown except the node which is not possible and the node step which is repeated. 
  Sample: Nodes.txt file
   1 4 7 0 2 8 3 5 6 
   1 4 7 2 0 8 3 5 6 
   1 4 7 3 2 8 0 5 6 
   0 4 7 1 2 8 3 5 6 
   ...

   2. "nodeInfo.txt" 
  Information regarding each node i.e the current node index and its parent index is generated for each node in the tree. 
  Where first column is Node index and second column is the parent index. 
  Sample: nodeInfo.txt file 
  1 0 0 
  2 1 0 
  3 1 0 
  4 2 0 
  ...

  3. "nodePath.txt"
  A step by step node flow of nodes is printed such that the final destination is reached from the given node.
  Note: If the input is not solvable or invalid, there error message is shown on the command prompt. 
  Sample: nodePath.txt file 
   1 4 7 0 2 8 3 5 6 
   1 4 7 2 0 8 3 5 6 
   1 4 7 2 5 8 3 0 6 
   1 4 7 2 5 8 3 6 0 

