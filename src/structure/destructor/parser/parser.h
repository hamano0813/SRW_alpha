#define PY_SSIZE_T_CLEAN
#include <Python.h>

#pragma pack(1)

#define codec "shiftjisx0213"

PyObject *replace(PyObject *text, PyObject *dict);