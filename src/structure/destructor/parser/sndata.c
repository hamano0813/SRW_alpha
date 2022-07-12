#include "parser.h"

typedef struct
{
    UINT32 quantity;
    UINT32 length;
    UINT32 indexes[0x10];
    char body[0x4000];
} Scenario;

typedef struct
{
    UINT32 场景指针[0x200];
    Scenario 场景数据[0x8C];
} SNDATA;

static PyObject *SNDATA_parse(PyObject *self, PyObject *args, PyObject *kwargs)
{
    PyObject *BufByte;
    char *kw_list[] = {"buf", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "Y", kw_list, &BufByte))
        return NULL;

    SNDATA *场景设计 = (SNDATA *)PyByteArray_AsString(BufByte);

    for (UINT32 i = 0; i < 0x8C; i++)
    {
        printf("%d\t%X\n", i, 场景设计[0].场景数据[i].quantity);
    }
}

const char parse_doc[] = "parse(buf: bytearray) -> dict";
const char build_doc[] = "build(data: dict) -> bytearray";

static PyMethodDef SNDATAMethods[] =
    {
        {"parse", (PyCFunction)SNDATA_parse, METH_VARARGS | METH_KEYWORDS, parse_doc},
        //{"build", (PyCFunction)SNDATA_build, METH_VARARGS | METH_KEYWORDS, build_doc},
        {NULL, NULL, 0, NULL}};

static struct PyModuleDef SNDATA_module =
    {
        PyModuleDef_HEAD_INIT,
        "SNDATA",
        "SNDATA.bin Parser",
        -1,
        SNDATAMethods};

PyMODINIT_FUNC PyInit_SNDATA(void)
{
    PyObject *module;
    module = PyModule_Create(&SNDATA_module);
    if (module == NULL)
        return NULL;
    return module;
}
