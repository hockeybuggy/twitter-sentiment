/*
 * File       : cminus.y
 * Author     : Douglas Anderson
 * Description: Lex specification for cminus
 */

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "globals.h"
#include "scan.h"
#include "parse.h"

#define YYPARSER
#define YYSTYPE void*

/*static char prev_token[MAX_TOKEN_LEN+1];*/

extern int yychar;

int yyerror(char* message){
    /*printf("Syntax error at line: %d \n", lineno);*/
    printf("%s \n", message);
    return(0);
}

static int yylex(void){
    /*strncpy(prev_token, token_string, MAX_TOKEN_LEN);*/
    return get_token();
}

void parse(void){
    yyparse();
    return;
}

%}

 /* Tokens*/
%token WORD
%token USER
%token HASHTAG
%token URL
 /* Danger Will Robinson; danger*/
%token ERROR

%%

tweet         : tweet token
              | token
token         : WORD
              | USER
              | HASHTAG
              ;

