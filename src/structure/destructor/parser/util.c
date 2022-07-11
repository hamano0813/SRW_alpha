#include "parser.h"

PyObject *replace(PyObject *text, PyObject *dict)
{
    PyObject *key, *value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(dict, &pos, &key, &value))
    {
        text = PyUnicode_Replace(text, key, value, -1);
    }
    return text;
}