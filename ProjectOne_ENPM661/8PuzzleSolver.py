import numpy as np
import copy as cp
from datetime import datetime
import sys


#print(datetime.now())
REQUIRED_RESULT = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
STEPS = []
NODE_QUEUE = []
TREE_QUEUE = []

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
		self.getOLocation()
		self.addToTree()

	#Method of Node Class, to check the inversion of the cube formation and add the node to tree
	#self: Object of Node
	def addToTree(self):
		OneD_cube = list((np.array(self.cube)).ravel())
		OneD_cube.remove(0)

		inv_count = 0
		for i in range(8):
			for j in range (i+1,8):
				if (OneD_cube[i]>OneD_cube[j]):
					inv_count = inv_count+1

		if inv_count%2 == 0:
			self.isSolvable = True 
		else:
			self.isSolvable = False
		TREE_QUEUE.append(self.cube)
		NODE_QUEUE.append(self)

	#Method of Node Class, to check if the newCube formed already exists in the tree else create a new node
	#self: Object of Node
	#newCube: 2D array of a new cube formation
	def checkAndCreateNode(self, newCube):
		if newCube in TREE_QUEUE:
			TREE_QUEUE.append("REPEAT")
			NODE_QUEUE.append("REPEAT")
		else:
			Node(self, newCube)

	#Method of Node Class, to generate the Moves
	#self: Object of Node
	def generateMoves(self):
		self.moveDown()

	#Method of Node Class, to save the 0 Location in the Node
	#self: Object of Node
	def getOLocation(self):
		for x, i in enumerate(self.cube):
			for y, j in enumerate(i):
				if j == 0:
					self.OLocation_x = x
					self.OLocation_y = y 

	#Method of Node Class, to generate the formation of the cube when the 0 moves down and appends to the Nodes queue
	#self: Object of Node
	def moveDown(self):
		if(self.OLocation_x != 2): #The 0 is not in the last row
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x+1][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x+1][self.OLocation_y]
			self.checkAndCreateNode(newCube)
			if newCube != REQUIRED_RESULT:
				self.moveRight()
		else:
			NODE_QUEUE.append(None)
			self.moveRight()

	#Method of Node Class, to generate the formation of the cube when the 0 moves right and appends to the Nodes queue
	#self: Object of Node
	def moveRight(self):
		if(self.OLocation_y != 2): #The 0 is not in the last coloumn
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x][self.OLocation_y+1], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y+1]
			self.checkAndCreateNode(newCube)
			if newCube != REQUIRED_RESULT:
				self.moveLeft()
		else:
			NODE_QUEUE.append(None)
			self.moveLeft()

	#Method of Node Class, to generate the formation of the cube when the 0 moves left and appends to the Nodes queue
	#self: Object of Node
	def moveLeft(self):
		if(self.OLocation_y != 0): #The 0 is not in the first coloumn
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x][self.OLocation_y-1], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y-1]
			self.checkAndCreateNode(newCube)
			if newCube != REQUIRED_RESULT:
				self.moveUp()
		else:
			NODE_QUEUE.append(None)
			self.moveUp()

	#Method of Node Class, to generate the formation of the cube when the 0 moves up and appends to the Nodes queue
	#self: Object of Node
	def moveUp(self):
		if(self.OLocation_x != 0): #The 0 is not in the first row
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x-1][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x-1][self.OLocation_y]
			self.checkAndCreateNode(newCube)
		else:
			NODE_QUEUE.append(None)



#Method to generate the path to the root node from the selected node
#fromNode: object of class Node
def generatePath(fromNode):
	while fromNode != None:
		STEPS.append(fromNode.cube)
		fromNode = fromNode.parent


#Method to Write the steps or the cube formation from the Given formation to the Required state
def printPath():
	if(len(STEPS) == 0):
		f_nodePath.write("-----------------------------------\n")
		f_nodePath.write("NOT A SOLVALBLE ENTRY")
		print("NOT A SOLVALBLE ENTRY")
	else:
		for x in reversed(STEPS):
			f_nodePath.write("-----------------------------------")
			f_nodePath.write("\n")
			try:
				for line in x:
					f_nodePath.write(" ".join([str(i) for i in line]))
					f_nodePath.write("\n")
			except AttributeError:
				f_nodePath.write("NONE\n")
			except TypeError:
				f_nodePath.write("NONE\n")
				continue

#Method to Write the All the cube formation from the Given formation to the Required state
def printNodes():
	f_nodes.write(" TOTAL NUMBER OF NODES: %d \n"%len(NODE_QUEUE))
	for i in NODE_QUEUE:
		f_nodes.write("----------------------------- \n")
		try:
			if i == None:
				f_nodes.write(" NOT POSSIBLE MOVE \n")
			else:
				if i == "REPEAT":
					f_nodes.write(" REPEATED NODE \n")
				else:
					if i.cube:
						for line in i.cube:
							f_nodes.write(" ".join([str(val) for val in line]))
							f_nodes.write("\n")
		except:
			continue

#Method to check if the given cube formation values are valid
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

#Method to print the error or success message and exit the puzzle 
#Message - String, value of the message
def exitPuzzle(Message):
	print(Message)
	f_nodes.close()
	f_nodePath.close()
	#print(datetime.now())
	sys.exit()



try:
	f_nodePath = open("nodePath.txt","w")
	f_nodes = open("Nodes.txt","w")
	givenCube = list(map(int, sys.argv[1].split()))
	cubeFormat = []

	if validEntry(givenCube) == True:
		for x in range(0,9,3):
			sliceObj = slice(x, x+3)
			cubeFormat.append(givenCube[sliceObj])
		root = Node(None, cubeFormat)
	else:
		raise ValueError
except IndexError:
	exitPuzzle("INVALID ARGUMENT ENTRY")
except ValueError:
	exitPuzzle("INVALID ENTRY")

#To expand the tree further inorder to reach the required node
for topNode in NODE_QUEUE:
	try:
		if(topNode.cube == REQUIRED_RESULT):
			generatePath(topNode)
			printPath()
			break
		else:
			if topNode.isSolvable == True:
				topNode.generateMoves()
			else:
				continue
	except AttributeError:
		continue

printNodes()
printPath()
exitPuzzle("FOUND SOLUTION!!!")
