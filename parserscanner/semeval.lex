/*
 * File       : cminus.lex
 * Author     : Douglas Anderson
 * Description: Lex specification for parser scanner
 */

%{
#include <stdlib.h>
#include <string.h>

#include "globals.h"
#include "scan.h"
#include "y.tab.h"

// Definition of global lineno
int lineno;
// Definition of global token_string
char token_string[MAX_TOKEN_LEN+1];

%}


digit       [0-9]
number      {digit}+
letter      [_a-zA-Z]
newline     \n
whitespace  [ \t]+
punct       [\+&%?!:,.;"]
word        ('|-|{digit}|{letter})+
url         https?:\/\/*[-A-Za-z0-9\+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#\/%=~_|]
hashtag     #{word}
user        @{word}

%%
 /*Stolen from http://stackoverflow.com/questions/161738 */

{url}     {return URL;}
{hashtag} {return HASHTAG;}
{user}    {return USER;}
{word}    {return WORD;}
{punct}   {return PUNCT;}

 /*TODO Emoticons*/

{whitespace}    { /* Whitespace */ }
{newline}       { /* Newline */ }
.               { return ERROR;}

%%

void init_parser(){
    yyin  = data_file;
    yyout = output_file;
}

int get_token(){
    int currentToken;
    currentToken = yylex();
    strncpy(token_string, yytext, MAX_TOKEN_LEN);
    return currentToken;
}
