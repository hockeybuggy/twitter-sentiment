/*
 * File       : scanner_module.c
 * Author     : Douglas Anderson
 * Description: wrapper for my parser to be driven from python
 */

#include <Python.h>
#include <stdlib.h>
#include "scan.h"

static PyObject* py_init_scanner(PyObject* self , PyObject* args){
    char *s = NULL;
    int result = 0;
    PyArg_Parse(args, "s", &s);
    printf("Init input: %s\n", s);
    init_scanner(s);
    return Py_BuildValue("i", result);
}

static PyObject* py_get_token(PyObject* self , PyObject* args){
    char *s = "Hello world";
    return Py_BuildValue("s", s);
}

static PyMethodDef scanner_module_methods[] = {
    {"init_scan", py_init_scanner},
    {"get_token", py_get_token},
    {NULL, NULL}
};

void initscanner_module(){
    (void) Py_InitModule("scanner_module", scanner_module_methods);
}
