#Emily Costa
'''
29/04/2019

Estrutura de Dados II

Árvore Rubro-Negra
'''

#Red-Black tree
'''
1. A node is either red or black
2. The root and leaves (NIL) are black
3. If a node is red, the its children are black
4. All paths from a node to its NIL descendants contain the same number of black nodes

obs:

*Nodes require one storage bit to keep track of color 
* THe longest path (root to farthest NIL) is no more than twice the length of the shortest 
path (root to nearest NIL):
    -> Shortest path: all black nodes
    -> Longest path: alternating red and black
'''

#Operations:

'''
Search
Insert -- require rotation
Remove -- require rotation
'''

#Inserção
''' 
legenda
[] = vermelho |  {} = preto

Caso 1:
Um nó sempre é inserido na cor vermelha, assim não altera a altura negra da árvore

Caso 2:
Ao inserir 'x', se o tio é vermelho, é necessário recolorir {a,t,p}

     {a}                     [a]
    /   \                   /   \
   [t]  [p]      --->     {t}   {p}
          \                       \
          [x]                     [x]

Caso 3:
O tio do elemento inserido é preto. Neste caso, para manter o critério (4) é preciso fazer rotações envolvendo 'a','t','p','x'
    *4 subcasos:
        Rotação a esquerda e direita
        Rotação dupla direita e esquerda

'''

#Remoção
'''
Caso 1: (Remoção Preguiçosa)
    Marca-se o nó como removido, mas sem tirá-lo da árvore
    Não precisa de remanejamento
    Algoritmos de inserção e busca devem ser notificados que o nó foi removido

Caso 2:
    Trocar id com nó sucessor
    Coloração não é alterada
    Remover então da subárvore do sucessor
''' 

