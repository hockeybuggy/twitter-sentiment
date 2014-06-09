/*
 * File       : globals.h
 * Author     : Douglas Anderson
 * Description: This header contains the declarations of the various global variables.
 */

#define MAX_TOKEN_LEN 140

// The following symbols are defined in main.c

// Global input file pointer
extern FILE* data_file;
// Global output file pointer to communicate to the user.
extern FILE* output_file;

// The following symbols are defined in cminus.lex

// Global token string declaration
extern char token_string[MAX_TOKEN_LEN+1];
