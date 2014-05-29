/*
 * File       : scan.h
 * Author     : Douglas Anderson
 * Description: This header declares the functions used in semevel.lex
 */

#ifndef _SCAN_H
#define _SCAN_H

// This function tells the lexer which files to use as input and output
void init_parser();

// This function copies the current yytext into the global token_string
int get_token();

#endif
