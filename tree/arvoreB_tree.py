#Emily Costa
'''
30/04/2019

Estrutura de Dados II
Material de Apoio: https://www.youtube.com/watch?v=oxTVYaKGg2A

'''


#Árvore B

'''
Árvore de busca em que cada nodo (ou página) contém mais de 1 elemento

Cada nodo possui vário filhos, bem parecido com árvore de busca binária

Cresce Para cima
'''

#Ordem na árvore B
'''
-> Autores
    *Número mínimo de elementos que cada pág ina (exceto raíz) pode ter (Cormen, Bayer e McCreight) [Vou Utilizar]
    Exemplo:
        Árvore de ordem 2 = mínimo 2 filhos e máximo 4 filhos, pois o número mínimo é 50% da capacidade
    *Número de filhos que cada página pode ter (Knuth)
'''
#Regras Árvore B
'''
    *Cada página deve ter pelo menos 50% de ocupação (ordem da árvore), exceto raíz
    *O número de filhos (exceto folha) deve ser o número de chaves + 1
    Exemplo:
        Se existem 2 chaves no nodo, necessariamente devem existir 3 filhos
    *Todas as folhas estão no mesmo nível (O crescimento é para cima)
'''
#Inserção
'''
*Se o elemento couber na página, basta incluí-lo de forma ordenada
*Se não couber, a página deve ser dividida em duas e o elmento do meio deve ser promovido
'''

#Remoção 
'''

Caso 1:
    Se o elemento estiver em uma folha e a folha mantiver 50% de ocupação, basta removê-lo
Caso 2:
    Se o elemento NÃO ESTIVER em uma folha, trocá-lo pelo seu antecessor
Caso 3:
    Se a folha ficar com menos de 50% de ocupação, mas a página irmã puder ceder uma chave
Caso 4:
    Se afolha ficar com menos de 50% de ocupação e as páginas irmãs não puderem ceder uma chave

obs:
    *Sempre vai acontecer na folha, caso o elemento a ser removido não seja folha, trocar por alguém na folha e remover na folha
    *Quanto maior o tamanho da página menor a quantidade de páginas e de níveis
    *Extremamente eficiente
    *Árvore B+, variação da árvore B muito utilizada em Banco de Dados 
'''

#Estrutura da Página (tamanho fixo)
'''
Material de Apoio: https://www.youtube.com/watch?v=XkPFu0IsQqo

----------------------------------------------------
|N| Po| CoDo|P1| C1D1|P2|C2D2|...|Pn-1|Cn-1Dn-1|Pn |
----------------------------------------------------
Em que:
    N  = Número de ELementos Presentes na página
    Ci = Chave do Registro (geralmente um código)     -- Registro da árvore
    Di = Dados (ex: endereço do registro no arquivo)  -- Registro da árvore
    Pi = Ponteiro para o i-ésimo filho

'''

