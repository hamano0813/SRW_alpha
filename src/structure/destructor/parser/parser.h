#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define CHAR unsigned char
#define BYTE char
#define WORD short
#define DOUBLE int

#define codec "shiftjisx0213"

#pragma pack(1)

PyObject *replace(PyObject *text, PyObject *dict);