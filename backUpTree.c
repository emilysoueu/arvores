//************************************************************************************************
#include <stdio.h>
#include <stdlib.h>

typedef struct _node{

	char dado;
	struct _node* filhoEsq;
	struct _node* filhoDir;
}node;

node* criar(char dado){
	node* tree = (node*)malloc(sizeof(node));
	if (tree == NULL) return NULL;

	tree -> dado = dado;
	tree -> filhoDir = NULL;
	tree -> filhoEsq = NULL;

	return tree;

}

node* filhoEsquerdo(node* raiz, char dado){
	node* temp = criar(dado);

	raiz->filhoEsq = temp;

}

node* filhoDireito(node* raiz, char dado){
	node* temp = criar(dado);

	raiz->filhoDir = temp;

}

int imprimir(node* raiz){ // Preorder = visitar ---- <raiz><esquerda><direita>
    if (raiz == NULL) return 0;
    imprimir(raiz->filhoEsq);
	printf("%c ", raiz->dado);
    imprimir(raiz->filhoDir);
}

/** ==============================CALCULAD0RA============================================ */

char token;

node* exp(void);
int term(void);
int fator(void);

void error(void){
	printf(stderr,"Error\n");
	exit(1);
}

void match (char tokenEsperado){
	if (token == tokenEsperado)
		token = getchar();
	else
		error();
}

int main(void) {
	int resultado;
	token = getchar(); /* Carga de marca com primeiro caractere com verificação a frente*/

	resultado = exp();

	if (token == '\n') /*teste final de linha*/
		printf("Resultado = %d\n", resultado);
	else
		error();/*Caracteres indevidos na linha*/
		return 0;

}

/**
int exp(void){
	int temp = term();
	while((token == '+')||(token == '-') ||(token == '/') ||(token =='%')){
		switch(token){
			case '+': match('+');
					temp += term();
			break;
			case '-': match('-');
					temp -= term();
			break;
            case '/': match('/');
                   	temp /= term();
            break;
            case '%': match('%');
                    temp = temp%term();
            break;
		}
		return temp;
	}
}
*/



node* exp(void){
	node* temp;
	node* novaTemp;

	temp = term();

	while((token == '+')||(token == '-') ||(token == '/') ||(token =='%')){
	    switch(token){
			case '+': match('+');
                    novaTemp = criar('+');
                    novaTemp =  filhoEsquerdo(novaTemp,temp);
                    novaTemp =  filhoDireito(novaTemp,term);
					temp = novaTemp;
					imprimir(temp);
					return temp;

			break;

        }


	}

}

int factor(void){
	int temp;

	if (token == '('){
		match ('(');
		temp = exp();
		match(')');
	}else if (isdigit(token)){
		ungetc(token,stdin);
		scanf("%d", &temp);
		token = getchar();
	}else
		error();
    return temp;

}

int term(void){
	int temp = factor();

	while(token == '*'){
		match('*');
		temp *= factor();
	}
	return temp;
}
/** ==============================CALCULAD0RA============================================ */







/**
int main(){
    node* raiz = NULL; // criando uma arvore vazia
     raiz = criar('+'); raiz = filhoEsquerdo(raiz,'2'); raiz = filhoDireito(raiz,'9');
     imprimir(raiz);
}
*/
