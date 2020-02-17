import numpy as np
import copy as cp
from datetime import datetime


print(datetime.now())
f = open("nodeData.txt","w")
REQUIRED_RESULT = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
STEPS = []
NODE_QUEUE = []
TREE_QUEUE = []

class Node:

	def __init__(self, parent, cube):
		self.parent = parent
		self.isSolvable = False
		self.OLocation_x = None
		self.OLocation_y = None
		self.cube = cube
		self.getOLocation()
		self.addToTree()

	def addToTree(self):
		#if self.cube in TREE_QUEUE:
		#	TREE_QUEUE.append(None)
		#	NODE_QUEUE.append(None)
		#else:
		Dcube = list((np.array(self.cube)).ravel())
		Dcube.remove(0)
		#count for Inversions
		inv_count = 0
		for i in range(8):
			for j in range (i+1,8):
				if (Dcube[i]>Dcube[j]):
					inv_count = inv_count+1

		if inv_count%2 == 0:
			self.isSolvable = True 
		else:
			self.isSolvable = False
		TREE_QUEUE.append(self.cube)
		NODE_QUEUE.append(self)

			#self.generateMoves() #Generates all the possible cases for each node
	def checkandAdd(self, newCube):
		if newCube in TREE_QUEUE:
			TREE_QUEUE.append(None)
			NODE_QUEUE.append(None)
		else:
			Node(self, newCube)

	def generateMoves(self):
		#if(self.cube[2][2] != 0):
				self.moveDown()

	def getOLocation(self):
		for x, i in enumerate(self.cube):
			for y, j in enumerate(i):
				if j == 0:
					self.OLocation_x = x
					self.OLocation_y = y 

	def moveDown(self):
		if(self.OLocation_x != 2): #The 0 is not in the last row
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x+1][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x+1][self.OLocation_y]
			#Node(self, newCube)
			self.checkandAdd(newCube)
			if newCube != REQUIRED_RESULT:
				self.moveRight()
		else:
			#TREE_QUEUE.append(None)
			NODE_QUEUE.append(None)
			self.moveRight()


	def moveRight(self):
		if(self.OLocation_y != 2): #The 0 is not in the last coloumn
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x][self.OLocation_y+1], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y+1]
			#Node(self, newCube)
			self.checkandAdd(newCube)
			if newCube != REQUIRED_RESULT:
				self.moveLeft()
		else:
			#TREE_QUEUE.append(None)
			NODE_QUEUE.append(None)
			self.moveLeft()


	def moveLeft(self):
		#print("moving left")
		if(self.OLocation_y != 0): #The 0 is not in the first coloumn
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x][self.OLocation_y-1], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y-1]
			#Node(self, newCube)
			self.checkandAdd(newCube)
			if newCube != REQUIRED_RESULT:
				self.moveUp()
		else:
			#TREE_QUEUE.append(None)
			NODE_QUEUE.append(None)
			self.moveUp()


	def moveUp(self):
		if(self.OLocation_x != 0): #The 0 is not in the first row
			newCube = cp.deepcopy(self.cube)
			newCube[self.OLocation_x-1][self.OLocation_y], newCube[self.OLocation_x][self.OLocation_y] = newCube[self.OLocation_x][self.OLocation_y], newCube[self.OLocation_x-1][self.OLocation_y]
			self.checkandAdd(newCube) 
			#Node(self, newCube)
			#if newCube != REQUIRED_RESULT:
			#	print("-")
		else:
			#TREE_QUEUE.append(None)
			NODE_QUEUE.append(None)


def generatePath(fromNode):
	while fromNode != None:
		STEPS.append(fromNode.cube)
		fromNode = fromNode.parent

def printPath():
	if(len(STEPS) == 0):
		f.write("-----------------------------------\n")
		f.write("Not a solvable entry")
	else:
		for x in reversed(STEPS):
			f.write("-----------------------------------")
			f.write("\n")
			try:
				for line in x:
					f.write(" ".join([str(i) for i in line]))
					f.write("\n")
			except AttributeError:
				f.write("NONE\n")
			except TypeError:
				f.write("NONE\n")
				continue


#root = Node(None, [[1, 2, 3], [4, 5, 6], [7, 0, 8]])
root = Node(None, [[1, 8, 2], [0, 4, 3], [7, 6, 5]])
#root = Node(None, [[1, 2, 3], [8, 6, 4], [7, 0, 5]]) #ppt case
#root = Node(None, [[1, 4, 7], [0, 2, 8], [3, 5, 6]]) #test case
#root = Node(None, [[0, 1, 3], [4, 2, 5], [7, 8, 6]])

for topNode in NODE_QUEUE:
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

printPath()
f.close()

print("size of the NODE_QUEUE: %d" %len(NODE_QUEUE))
print("Number of STEPS: %d" %len(STEPS))
print(datetime.now())
