# -*- coding: utf-8 -*-
'''
@parameters:
v = vetor
p = pos inic
r = pos fim
x = elemento procurado
'''
#só funciona se o vetor estiver ordenado

def busca_binaria(v,p,r,x):

    if p <= r :#procurar enquanto o vetor tiver pelo menos um elemento (condição de parada ou existência)
        q = (p+r)//2 #encontrar o índice do meio do vetor
        if x > v[q]: #elemento procurado esta a direita
            return busca_binaria(v, q+1, r, x)
        elif x < v[q] :#elemento procurado esta a esquerda
            return busca_binaria(v, p, q-1,x)
        else:
            return q # elemento procurado ja é o meio

    return -1 # caso não encontre
	
vetor = list(range(0,10))
print(vetor)

chave = 9
posicao = busca_binaria(vetor, 0, len(vetor)-1,chave)


if posicao >= 0:
    print("O elemento %d foi encontrado em %d" %(chave,posicao))
else:
    print("O elemento nao foi encontrado")



