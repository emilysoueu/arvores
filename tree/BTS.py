#Binary Search Tree in Python

'''
Material de Apoio:
Vídeo 1: https://www.youtube.com/watch?v=f5dU3xoE6ms&t=153s
Vídeo 2: https://www.youtube.com/watch?v=6oL-0TdVy28

'''

class Node(object):
    def __init__(self, val):
        self.value = val # dado
        self.left = None # ponteiro pro filho a esquerda
        self.right = None #ponteiro pro filho a direita

    

class Tree(object):
    def __init__(self):
        self .root = None

    def insert (self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)
    
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value,cur_node.left)
        elif value >cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value,cur_node.right)
        else:
            print ("Value alredy in tree")
    
    '''
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
    
    def _print_tree(self,cur_node): #inOrder
        if cur_node != None:
            self._print_tree(self,cur_node.left)
            self._print_tree(self,cur_node.value)
            self._print_tree(self,cur_node.right)
    '''

    def mostra(self):
        if self.root != None:
            self.printArvore(self.root)

    def printArvore(self,root):
        if self.root!=None:
            print(self.root.left.value)
            print(self.root.value)            
            print(self.root.right.value)


    def find(self, data):
        if self.value == data:
            return True
        elif data > self.Node(data):
            find(self.left(data))
        else:
            find(self.right(data))



def fill_tree(tree,num_elems=10,max_int=10):
    from random import randint
    for _ in range (num_elems):
        cur_elem = randint(0,max_int)
        tree.insert(cur_elem)
    return tree


tree = Tree()
tree = fill_tree(tree)

tree.mostra()




     