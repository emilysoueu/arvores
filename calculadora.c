#include <stdio.h>
#include <stdlib.h>



	/* EBNF

	Casamaneto = chama getToken e pega o próximo
	Além de verificar a sintaxe ja faz o cálculo
	*/


	//Implementar uma calculadora para aritmética de inteiros simples segundo a EBNF

char token;

int exp(void);
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
