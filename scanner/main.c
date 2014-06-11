/*
 * File       : main.c
 * Author     : Douglas Anderson
 * Description: Driver for my parser implementation
 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "globals.h"
#include "scan.h"
#include "util.h"

FILE* data_file;
FILE* output_file;

void parse_input(){
    init_scanner(NULL); // Set up the input and output of the parser

    int token_type;
    while((token_type = get_token()) != 0){
        printToken(token_type, token_string);
        fprintf(output_file, "\n");
    }
    fclose(data_file);
}

int main(int argc, char* argv[]){
    if (argc == 1) {
        data_file = stdin;
    } else if (argc == 2) {
        data_file = fopen(argv[1], "r");
    } else {
        fprintf(stderr,"Usage: %s <filename>\n", argv[0]);
        return(1);
    }

    output_file = stdout;

    if(data_file == NULL){
        fprintf(stderr, "Error. File '%s' not found.\n", argv[2]);
        return(-1);
    }

    parse_input(); // Parses the input tsv file

    return(0);
}
