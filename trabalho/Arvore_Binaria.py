class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data):
		#For inserting the data in the Tree
		if self.data == data:
			return False        # As BST cannot contain duplicate data

		elif data[0] < self.data[0]:
			#Data less than the root data is placed to the left of the root
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
			return True

		else:
			#Data greater than the root data is placed to the right of the root
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
				return True

	def minValue(self, node):
		current = node

		# loop down to find the leftmost leaf
		while(current.left is not None):
			current = current.left

		return current

	def delete(self, data):
		if self is None:
			return None

		# if current node's data is less than that of root node, then only search in left subtree else right subtree
		if data < self.data[0]:
			self.left.delete(data)
		elif data > self.data[0]:
			self.right.delete(data)
		else:
			# deleting node with one child
			if self.left is None:
				temp = self.right
				self = None
				return temp
			elif self.right is None:
				temp = self.left
				self = None
				return temp

			# deleting node with two children
			# first get the inorder successor
			temp = self.minValue(self.right)
			self.data = temp.data
			self.right = self.right.delete(temp.data)

		return self

	def find(self, data):
		#checks whether the specified data is in tree or not
		if(data == int(self.data[0])):
			return True
		elif(data < int(self.data[0])):
			if self.left:
				return self.left.find(data)
			else:
				return False
		else:
			if self.right:
				return self.right.find(data)
			else:
				return False

	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder()
			print(str(self.data))

class Tree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root!=None:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True

	def delete(self, data):
		if self.root is not None:
			return self.root.delete(data)

	def find(self, data):
		if self.root!=None:
			return self.root.find(data)
		else:
			return False
	def postorder(self):
		print()
		if self.root is not None:
			self.root.postorder()
#============================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#============================================


#~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~
tree = Tree()
data=[]
caminho=raw_input("\nDigite o nome do arquivo\n")
with open(caminho) as arquivo:
	for line in arquivo:
		data.append(line.split(','))
print("\nInserindo elementos ...\n")
for key in data:
	tree.insert(key)
print(tree.postorder())
var=0
while(var!=4):
	print("\n1 - Printar arvore postorder\n")
	print("\n2 - Deletar elemento (pela chave)\n")
	print("\n3 - Encontrar elemento (pela chave)\n")
	print("\n4 - sair\n")
	var=int(input())
	if(var==1):
		os.system('cls' if os.name == 'nt' else 'clear')
		print(tree.postorder())
	elif(var==2):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\nInforme a chave\n")
		elm=int(input())
		tree.delete(elm)
	elif(var==3):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("\nInforme a chave\n")
		elm=int(input())
		result=tree.find(elm)
		print(result)
#~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~
