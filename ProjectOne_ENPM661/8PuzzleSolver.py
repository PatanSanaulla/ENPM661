import numpy as np
import copy as cp
from datetime import datetime
import sys

print(datetime.now())
REQUIRED_RESULT = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
STEPS = [] #list of 8 puzzle steps backtracked in list format []
MATRIX_8PUZZLE_NODES = [] #List of Node objects based on the order of generation.  
TREE_QUEUE = [] #List of cube tile values for all the created nodes

class Node:

	#Method to initialize the node with the values/attributes and add the Node
	#self: Object of class Node
	#parent: Object of class Node
	#Cube: the cube formation for the Node 
	def __init__(self, parent, cube):
		self.parent = parent
		self.isSolvable = False
		self.OLocation_x = None
		self.OLocation_y = None
		self.cube = cube
		self.blankTileLocation()
		self.addToTree()

	#addToTree - Method of Node Class, to check the inversion of the cube formation and add the node to tree
	#self: Object of Node
	def addToTree(self):
		OneD_cube = list((np.array(self.cube)).ravel()) #making the 2D array into list
		OneD_cube.remove(0) #removing the 0 to perform the solvabliity check 

		inv_count = 0 #inversion counter
		for i in range(8):
			for j in range (i+1,8):
				if (OneD_cube[i]>OneD_cube[j]):
					inv_count = inv_count+1

		if inv_count%2 == 0:
			self.isSolvable = True 
		else:
			self.isSolvable = False
		TREE_QUEUE.append(self.cube)
		MATRIX_8PUZZLE_NODES.append(self)

	#Method of Node Class, to check if the newCube formed already exists in the tree else create a new node
	#self: Object of Node
	#newCube: 2D array of a new cube formation
	def checkAndCreateNode(self, newCube):
		if newCube in TREE_QUEUE:
			#To Check if the node value is already in tree
			pass
		else:
			Node(self, newCube)

	#generateMoves - Method of Node Class, to generate the Moves
	#self: Object of Node
	def generateMoves(self):
		self.actionMoveDown()

	#blankTileLocation - Method of Node Class, to save the 0 Location in the Node
	#self: Object of Node
	def blankTileLocation(self):
		for x, i in enumerate(self.cube):
			for y, j in enumerate(i):
				if j == 0:
					self.OLocation_x = x
					self.OLocation_y = y 

	#actionMoveDown - Method of Node Class, to generate the formation of the cube when the 0 moves down and appends to the Nodes queue
	#self: Object of Node
	def actionMoveDown(self):
		if(self.OLocation_x != 2): #The 0 is not in the last row
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x+1][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x+1][self.OLocation_y]
			self.checkAndCreateNode(newCube)
			if newCube != REQUIRED_RESULT:
				self.actionMoveRight()
		else:
			self.actionMoveRight()

	#actionMoveRight - Method of Node Class, to generate the formation of the cube when the 0 moves right and appends to the Nodes queue
	#self: Object of Node
	def actionMoveRight(self):
		if(self.OLocation_y != 2): #The 0 is not in the last coloumn
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x][self.OLocation_y+1], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y+1]
			self.checkAndCreateNode(newCube)
			if newCube != REQUIRED_RESULT:
				self.actionMoveLeft()
		else:
			self.actionMoveLeft()

	#actionMoveLeft - Method of Node Class, to generate the formation of the cube when the 0 moves left and appends to the Nodes queue
	#self: Object of Node
	def actionMoveLeft(self):
		if(self.OLocation_y != 0): #The 0 is not in the first coloumn
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x][self.OLocation_y-1], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y-1]
			self.checkAndCreateNode(newCube)
			if newCube != REQUIRED_RESULT:
				self.actionMoveUp()
		else:
			self.actionMoveUp()

	#actionMoveUp - Method of Node Class, to generate the formation of the cube when the 0 moves up and appends to the Nodes queue
	#self: Object of Node
	def actionMoveUp(self):
		if(self.OLocation_x != 0): #The 0 is not in the first row
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x-1][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x-1][self.OLocation_y]
			self.checkAndCreateNode(newCube)



#generatePath - Method to generate the path to the root node from the selected node
#fromNode: object of class Node
def generatePath(fromNode):
	while fromNode != None:
		STEPS.append(fromNode.cube)
		fromNode = fromNode.parent


#printPath - Method to Write the steps or the cube formation from the Given formation to the Required state
def printPath():
	if(len(STEPS) == 0):
		f_nodePath.write("NOT A SOLVALBLE ENTRY")
		exitPuzzle("NOT A SOLVALBLE ENTRY")
	else:
		for step in reversed(STEPS):
			try:
				coloumn_wise = "" #To print the node in the file Coloumn Wise
				for col in range(3):
					coloumn_wise = coloumn_wise +" "+(" ".join([str(step[row][col]) for row in range(3)]))
				f_nodePath.write(coloumn_wise)
				f_nodePath.write("\n")
			except AttributeError:
				f_nodePath.write("NONE\n")
			except TypeError:
				f_nodePath.write("NONE\n")
				continue

#printNodesandInfo- Method to Write the All the cube formation from the Given formation to the Required state
def printNodesandInfo():
	for node in MATRIX_8PUZZLE_NODES:
		try:
			if node.cube:
				coloumn_wise = "" #To print the node in the file Coloumn Wise
				for col in range(3):
					coloumn_wise = coloumn_wise +" "+(" ".join([str(node.cube[row][col]) for row in range(3)]))
				f_nodes.write(coloumn_wise)
				f_nodes.write("\n")

				node_index = MATRIX_8PUZZLE_NODES.index(node)+1 #To print the index of node and parent node for nodes Info
				if node.parent == None:
					parent_index = 0
				else:
					parent_index = MATRIX_8PUZZLE_NODES.index(node.parent)+1
				f_nodeInfo.write(str(node_index)+" "+str(parent_index)+" "+'0')
				f_nodeInfo.write("\n")
		except:
			continue

#validEntry- Method to check if the given cube formation values are valid
#givenValue - an list of integer values
#returns - True if valid else False
def validEntry(givenValue):
	if len(set(givenValue)) == len(givenValue) & len(givenValue) == 9:
		for val in givenValue:
			if val>8 | val<0:
				return False
		return True
	else:
 		return False

#exitPuzzle- Method to print the error or success message and exit the puzzle 
#Message - String, value of the message
def exitPuzzle(Message):
	print(Message)
	f_nodes.close()
	f_nodePath.close()
	f_nodeInfo.close()
	print(datetime.now())
	sys.exit()



try:
	f_nodePath = open("nodePath.txt","w")
	f_nodes = open("Nodes.txt","w")
	f_nodeInfo = open("nodeInfo.txt","w")
	givenCube = list(map(int, sys.argv[1].split()))
	cubeFormat = []

	if validEntry(givenCube) == True:
		#Reading from Coloumn Arrangement to Row Arrangement
		for i in range(3):
			newRow = []
			for j in range (i,9,3):
				newRow.append(givenCube[j])
			cubeFormat.append(newRow)
		#Creating the root node with the given value of tiles	
		root = Node(None, cubeFormat)
	else:
		raise ValueError
except IndexError:
	exitPuzzle("INVALID ARGUMENT ENTRY")
except ValueError:
	exitPuzzle("INVALID ENTRY")

#To expand the tree further inorder to reach the required node
for topNode in MATRIX_8PUZZLE_NODES:
	try:
		if(topNode.cube == REQUIRED_RESULT):
			generatePath(topNode)
			break
		else:
			if topNode.isSolvable == True:
				topNode.generateMoves()
			else:
				continue
	except AttributeError:
		continue

printNodesandInfo()
printPath()
exitPuzzle("FOUND SOLUTION!!!")
