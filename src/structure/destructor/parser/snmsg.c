#include "parser.h"

typedef struct //文本列表
{
    CHAR msg[0x100]; //文本
} SNMSG;

static PyObject *SNMSG_parse(PyObject *self, PyObject *args)
{
    PyObject *ByteArray;
    PyObject *ExtraDict;
    PyObject *TransDict;
    if (!PyArg_ParseTuple(args, "YOO", &ByteArray, &ExtraDict, &TransDict))
        return NULL;
    BYTE *buffer;
    buffer = PyByteArray_AsString(ByteArray);
    if (!buffer)
        return NULL;

    Py_ssize_t count = (Py_ssize_t)(PyByteArray_Size(ByteArray) / sizeof(SNMSG));

    SNMSG *snmsg;
    snmsg = (SNMSG *)buffer;

    PyObject *msgs_val = PyList_New(0);

    for (DOUBLE msg_idx = 0; msg_idx < count; msg_idx++)
    {
        size_t msg_len = strlen((snmsg + msg_idx)->msg);
        PyObject *msg_val = PyUnicode_Decode((snmsg + msg_idx)->msg, msg_len, codec, "replace");

        msg_val = replace(msg_val, ExtraDict);
        msg_val = replace(msg_val, TransDict);

        PyObject *msg_dict = PyDict_New();
        PyDict_SetItem(msg_dict, Py_BuildValue("s", "文本"), msg_val);

        PyList_Append(msgs_val, msg_dict);
    }

    PyObject *output_dict = PyDict_New();

    PyDict_SetItem(output_dict, Py_BuildValue("s", "文本列表"), msgs_val);

    return output_dict;
}

static PyMethodDef SNMSGMethods[] =
    {
        {"parse", SNMSG_parse, METH_VARARGS, "parse SNMSG.bin data."},
        {NULL, NULL, 0, NULL}};

static struct PyModuleDef SNMSG_module =
    {
        PyModuleDef_HEAD_INIT,
        "SNMSG",
        "SNMSG.bin parser",
        -1,
        SNMSGMethods};

PyMODINIT_FUNC PyInit_SNMSG(void)
{
    PyObject *module;
    module = PyModule_Create(&SNMSG_module);
    if (module == NULL)
        return NULL;
    return module;
}
