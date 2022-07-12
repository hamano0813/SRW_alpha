#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdint.h>

#pragma pack(1)

#define codec "shiftjisx0213"

PyObject *replace(PyObject *text, PyObject *dict);

PyObject *decode(char *s, PyObject *extra, PyObject *trans);

char *encode(PyObject *unicode, PyObject *extra, PyObject *trans);
