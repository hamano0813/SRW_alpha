#include "parser.h"

#define BP_QTY 0x10
#define BP_LEN 0x4
#define b_count 0xB

typedef struct
{
    UINT8 code;
    UINT8 count;
    INT16 param[0];
} COMMAND;

typedef struct
{
    UINT32 QTY;
    UINT32 LEN;
    UINT32 indexes[0x10];
    char commands[0x4000];
} SNDATA;

static PyObject *SNDATA_parse(PyObject *self, PyObject *args, PyObject *kwargs)
{
    PyObject *BufByte;
    char *kw_list[] = {"buf", NULL};
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "Y", kw_list, &BufByte))
        return NULL;

    SNDATA *场景设计 = (SNDATA *)PyByteArray_AsString(BufByte);
    PyObject *ScenarioDict = PyDict_New();

    PyDict_SetItem(ScenarioDict, Py_BuildValue("s", "Index Quantity"), Py_BuildValue("i", BP_QTY));
    PyDict_SetItem(ScenarioDict, Py_BuildValue("s", "Index Length"), Py_BuildValue("i", BP_LEN));

    PyObject *BlockList = PyList_New(0);
    for (UINT8 b_idx = 0; b_idx < b_count; b_idx++)
    {
        PyObject *BlockDict = PyDict_New();
        PyDict_SetItem(BlockDict, Py_BuildValue("s", "Index"), Py_BuildValue("i", 场景设计[0].indexes[b_idx]));
        PyList_Append(BlockList, BlockDict);
    }
    PyDict_SetItem(ScenarioDict, Py_BuildValue("s", "Indexes"), BlockList);

    PyObject *CommandList = PyList_New(0);
    int offset = 0;

    while (场景设计[0].commands[offset] != -1)
    {
        UINT8 length = 场景设计[0].commands[offset + 1] * 2;

        char *command = (char *)calloc(length, sizeof(char));
        memcpy(command, 场景设计[0].commands + offset, length);
        COMMAND *指令 = (COMMAND *)command;

        PyObject *CommandDict = PyDict_New();
        PyDict_SetItem(CommandDict, Py_BuildValue("s", "Pos"), Py_BuildValue("i", offset / 2));
        PyDict_SetItem(CommandDict, Py_BuildValue("s", "Code"), Py_BuildValue("i", 指令[0].code));
        PyDict_SetItem(CommandDict, Py_BuildValue("s", "Count"), Py_BuildValue("i", 指令[0].count));

        PyObject *ParamList = PyList_New(0);
        for (UINT8 p_idx = 0; p_idx < (指令[0].count - 1); p_idx++)
            PyList_Append(ParamList, Py_BuildValue("i", 指令[0].param[p_idx]));
        switch (指令[0].code)
        {
        case 0x64:
            ParamList = PyList_New(0);
            PyList_Append(ParamList, Py_BuildValue("i", 指令[0].param[0] << 16 | 指令[0].param[1]));
            break;
        case 0x69:
            PyList_SetItem(ParamList, 1, Py_BuildValue("i", (UINT16)指令[0].param[1]));
            break;
        case 0x70:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0x7D:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0x83:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[1]));
            break;
        case 0x91:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0x93:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[1]));
            break;
        case 0x94:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0x97:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0x98:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[1]));
            break;
        case 0x9D:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0xA0:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0xAC:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[1]));
            break;
        case 0xAE:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[1]));
            break;
        case 0xB0:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[1]));
            break;
        case 0xB2:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        case 0xB8:
            PyList_SetItem(ParamList, Py_BuildValue("i", (UINT8)指令[0].param[0]));
            break;
        default:
            for (UINT8 p_idx = 0; p_idx < (指令[0].count - 1); p_idx++)
                PyList_Append(ParamList, Py_BuildValue("i", 指令[0].param[p_idx]));
            break;
        }

        free(command);
        PyDict_SetItem(CommandDict, Py_BuildValue("s", "Param"), ParamList);
        PyDict_SetItem(CommandDict, Py_BuildValue("s", "Data"), Py_BuildValue("s", " "));
        PyList_Append(CommandList, CommandDict);
        offset += length;
    }
    PyDict_SetItem(ScenarioDict, Py_BuildValue("s", "Commands"), CommandList);

    return ScenarioDict;
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
