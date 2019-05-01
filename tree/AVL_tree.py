'''
Emily Costa
28/04/2019
Estrutura de dados II

******* Árvore AVL *******
'''
#Como garantir o equilíbrio? ROTAÇÕES 

"""
O equilíbrio de uma árvore binária de busca é medido
subtraindo o número de níveis na sub-árvore da esquerda
do número de níveis da sub-árvore da direita
"""

#Após identificar o desequilíbrio, como fazer para equilibrar?

'''
Tipos de Rotação:
1) Rotação à esquerda
2) Rotação à direita
3) Rotação dupla à esquerda
4) Rotação dupla à esquerda
'''
#1) Rotação à esquerda
'''
* Filho da direita vira nova raiz 
(*)Caso tenha o nó da direira tenha um filho:
-> o filho a esquerda do nó a direita vira filho direito do nó a esquerda
* A raíz original vira filho da esquerda da nova raiz

1.                 2.
(a)                 (b)
   \                /  \
    (b)           (a)  (d)
    /  \            \
  (c)   (d)         (c)

'''

#2) Rotação à direita
'''
1.                      2.
       (c)                (b)  
       /                  / \ 
    (b)                 (a) (c)
    / \                     /  
 (a)  (d)                 (d) 

* (b) é a nova raíz
  (c) vira filho a direita de b (nó a esquerda)
  (d) filho a direira de (b) vira filho a esquerda de (c)

'''

#3) Rotação dupla à esquerda
'''
obs:
desequilíbrio (+) na raíz original e 
desequilíbrio (-) na sub-árvore mostra que
uma rotação simples não resolve o balanceamento

Passos:
1) Rotação à direita na sub-árvore da direita
2) Rotação à esquerda ma árvore original

            1.        2.
 (a)        (a)         (b)
   \          \         /  \
    (c)       (b)     (a)  (c)
    /           \
  (b)           (c)

'''
#4) Rotação dupla à esquerda

'''
Passos:
1) Rotação à esquerda na sub-árvore da esquerda
2) Rotação à direita ma árvore original

               1.         2.
     (c)        (c)        (b)
    /           /         /   \
  (a)         (b)        (a)  (c) 
    \         /
    (b)     (a)


'''

#Como decidir qual rotação devemos realizar?
'''
1. Calcular o fator de equilíbrio (Q) :
Q = R - L
    se -1 <= q <=1  [árvore equilibrada]
        se q > 1: 
            se a sub-árvore da direita tem q < 0
                rotação dupla à esquerda
            senão
                rotação a esquerda
    senão:
        se a sub-árvore da esquerda tem q > 0:
            rotação dupla à direita
        senão:
        rotação à direita
'''


