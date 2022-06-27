#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject* compressor_decompress(PyObject* self, PyObject* args)
{
	PyObject* InputByteArray;
	unsigned char* Input;

	if (!PyArg_ParseTuple(args, "Y", &InputByteArray))
	{
		return NULL; // Error already raised
	}

	Input = PyByteArray_AsString(InputByteArray);
	if (!Input)
	{
		return NULL; // Error already raised
	}

	int InputSize = (int)PyByteArray_Size(InputByteArray);
	int InputIndex = 0;

	unsigned int UnitCount;
	UnitCount = Input[InputIndex++];
	UnitCount += Input[InputIndex++] << 8;
	UnitCount += Input[InputIndex++] << 16;
	UnitCount += Input[InputIndex++] << 24;

	unsigned int* Pointer;
	Pointer = malloc(UnitCount);
	if(!Pointer)
	{
		return PyErr_NoMemory();
	}

    // Test
    PyObject* PointerList = PyList_New(UnitCount);

	for (int pointer_idx=0; pointer_idx< UnitCount; pointer_idx++)
	{
		Pointer[pointer_idx] = Input[InputIndex++];
        Pointer[pointer_idx] += Input[InputIndex++] << 8;
        Pointer[pointer_idx] += Input[InputIndex++] << 16;
        Pointer[pointer_idx] += Input[InputIndex++] << 24;

		// Test
        PyObject* pointer = Py_BuildValue("i", Pointer[pointer_idx]);
        PyList_SetItem(PointerList, pointer_idx, pointer);

	}

	return PointerList;
}

static PyMethodDef compressorMethods[] =
{
	{"decompress", compressor_decompress, METH_VARARGS, NULL},
	{NULL, NULL, 0, NULL} // Sentinel
};

static struct PyModuleDef compressor_module =
{
	PyModuleDef_HEAD_INIT,
	"compressor", // Module name
	NULL, // Documentation
	-1, // Size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
	compressorMethods
};

PyMODINIT_FUNC PyInit_compressor(void)
{
	PyObject* module;

	module = PyModule_Create(&compressor_module);
	if (module == NULL)
	{
		return NULL;
	}
	return module;
}
