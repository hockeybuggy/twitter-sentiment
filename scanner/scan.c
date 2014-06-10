/*
 * File       : scan.h
 * Author     : Douglas Anderson
 * Description: This header defines the functions to run the scanner
 */

#include <stdlib.h>
#include <string.h>

#include "lex.yy.h"
#include "globals.h"
#include "scan.h"

void init_scanner(char *inputstr){
    int tempfd;
    FILE* temp_file;
    yyin  = data_file;
    yyout = output_file;

    if(inputstr != NULL){
        tempfd = mkstemp("SEMEVAL_XXXXXX");
        temp_file = fdopen(tempfd, "r+");
        if(temp_file != NULL){
            fprintf(temp_file, "%s", inputstr);
        }

        yyin  = temp_file;
        /*yyout = NULL;*/
    } else {
    }
}

int get_token(){
    token_t currentToken;
    currentToken = yylex();
    strncpy(token_string, yytext, MAX_TOKEN_LEN);
    return currentToken;
}

