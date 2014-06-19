/*
 * File       : cminus.lex
 * Author     : Douglas Anderson
 * Description: Lex specification for parser
 */

%{
#include <stdlib.h>
#include <string.h>

#include "globals.h"
#include "scan.h"

// Definition of global token_string
char token_string[MAX_TOKEN_LEN+1];

%}


digit       [0-9]
number      ({digit}*\.)?{digit}+
letter      [_a-zA-Z]
newline     \n
whitespace  [ \t]+
punct       [\+&$%?\-_!:,.;<>'"\(\)\{\}\[\]]|\.{2,3}
wordpart    ({digit}|{letter})+
word        {wordpart}('{wordpart}|-{wordpart})*

hashtag     #{word}
user        @{word}

happy       :-?D+|:-?\)+|B-?\)+|8-?\)+|:-?p+
sad         :-?\(+|8-\(+|:'\(|;-?\)
wink        ;-?\)+|;-?D|;-?D|;-?p+
other       <+3+
emoticon    {happy}|{sad}|{wink}|{other}

url         https?:\/\/*[-A-Za-z0-9\+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#\/%=~_|]

%%

{url}     {return URL;}
{hashtag} {return HASHTAG;}
{user}    {return USER;}
{number}  {return NUMBER;}
{punct}   {return PUNCT;}
{word}    {return WORD;}
{emoticon}    {return EMOTICON;}

{whitespace}    { /* Whitespace */ }
{newline}       { /* Newline */ }
.               { return ERROR;}

%%

void init_scanner(char *inputstr){
    yyin  = data_file;
    yyout = output_file;
}

int get_token(){
    token_t currentToken;
    currentToken = yylex();
    strncpy(token_string, yytext, MAX_TOKEN_LEN);
    return currentToken;
}

