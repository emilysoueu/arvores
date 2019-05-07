//************************************************************************************************
// executar no terminal

//$ gcc prog.c -o prog
//$ ./prog


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
	//tree -> filhoDir = NULL;
	//tree -> filhoEsq = NULL;

	//printf("Raiz (Operacao)criada com sucesso\n");
	//printf("Dado: %c",tree->dado,"\n" );

	return tree;

}

node* filhoEsquerdo(node* raiz, char dado){
	node* temp = criar(dado);

	if (raiz!= NULL)
		raiz->filhoEsq = temp;
	else
		printf("Erro ao inserir filho esquerdo -> Raiz Nula\n");

}

node* filhoDireito(node* raiz, char dado){
	node* temp = criar(dado);

	if (raiz!=NULL)
		raiz->filhoDir = temp;
	else
		printf("Erro ao inserir filho direito -> Raiz Nula\n");


}

int imprimir(node* raiz){ // Preorder = visitar ---- <raiz><esquerda><direita>
    if (raiz == NULL) return 0;

    imprimir(raiz->filhoEsq);
	printf("%c ", raiz->dado);
    imprimir(raiz->filhoDir);
}

/** ======================================CALCULAD0RA============================================ */

char token;

node* exp(void);
int term(void);
int fator(void);

void error(void){
	printf(stderr,"Error\n");
	exit(1);
}

// funcão casamento
void match (char tokenEsperado){
	if (token == tokenEsperado)
		token = getchar();
	else
		error();
}

int main(void) {

	node* resultado;

	printf("Insira a expresao:\n");
	token = getchar(); /* Carga de marca com primeiro caractere com verificação a frente*/ //(2+2)
	printf("Token:",token,"\n" );


	
	resultado = exp(); //2+2
	//printf("\nResultado main 1:",resultado,"\n" );
	printf("\n\n");

	printf("\nResultado main  = %d\n", resultado);
	


	// if (token == '\n') /*teste final de linha*/
	// 	printf("\nResultado main 2 = %d\n", resultado);
	// else
	// 	error();/*Caracteres indevidos na linha*/
	// 	return 0;

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
	node* temp;     // provavelmente problemas com os tipos ja que ta node mas acho que deveria ser char
	node* novaTemp;

	temp = term();

	while((token == '+')||(token == '-') ||(token == '/') ||(token =='%')){
	    switch(token){
			case '+': match('+');
                    novaTemp = criar('+');
                    novaTemp =  filhoEsquerdo(novaTemp,'2'); // inserido na força bruta
                    novaTemp =  filhoDireito(novaTemp,'2'); // inserido na força bruta
					temp  = novaTemp; 


					printf("Árvore Inserida:\n");
					imprimir(temp);
					printf("\n");

					
					
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




