#include "parser.h"

typedef struct //文本列表
{
    CHAR msg[0x100]; //文本
} SNMSG;

const char parse_doc[] = "parse(buffer: bytearray, extra: dict, trans: dict) -> dict";

static PyObject *SNMSG_parse(PyObject *self, PyObject *args, PyObject *kwargs)
{
    PyObject *BufBytearray;
    PyObject *ExtraDict;
    PyObject *TransDict;
    char *kw_list[] = {"buffer", "extra", "trans", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "YOO", kw_list, &BufBytearray, &ExtraDict, &TransDict))
        return NULL;
    CHAR *data_char;
    data_char = PyByteArray_AsString(BufBytearray);
    if (!data_char)
        return NULL;

    DOUBLE msg_count = (DOUBLE)(PyByteArray_Size(BufBytearray) / sizeof(SNMSG));

    SNMSG *snmsg_ptr;
    snmsg_ptr = (SNMSG *)data_char;

    PyObject *MsgList = PyList_New(0);

    for (DOUBLE msg_idx = 0; msg_idx < msg_count; msg_idx++)
    {
        size_t msg_len = strlen((snmsg_ptr + msg_idx)->msg);
        PyObject *MsgStr = PyUnicode_Decode((snmsg_ptr + msg_idx)->msg, msg_len, codec, "replace");

        MsgStr = replace(MsgStr, ExtraDict);
        MsgStr = replace(MsgStr, TransDict);

        PyObject *MsgDict = PyDict_New();
        PyDict_SetItem(MsgDict, Py_BuildValue("s", "文本"), MsgStr);

        PyList_Append(MsgList, MsgDict);
    }

    PyObject *DataDict = PyDict_New();
    PyDict_SetItem(DataDict, Py_BuildValue("s", "文本列表"), MsgList);

    return DataDict;
}

static PyMethodDef SNMSGMethods[] =
    {
        {"parse", (PyCFunction)SNMSG_parse, METH_VARARGS | METH_KEYWORDS, parse_doc},
        {NULL, NULL, 0, NULL}};

static struct PyModuleDef SNMSG_module =
    {
        PyModuleDef_HEAD_INIT,
        "SNMSG",
        "SNMSG.bin Parser",
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
