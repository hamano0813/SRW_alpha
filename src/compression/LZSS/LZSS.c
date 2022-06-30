#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define MAXEXPAND 0x12

int32_t ReadInt(uint8_t *Buffer, int32_t Offset)
{
	uint32_t Value;
	Value = Buffer[Offset++];
	Value += Buffer[Offset++] << 8;
	Value += Buffer[Offset++] << 16;
	Value += Buffer[Offset] << 24;
	return Value;
}

void WriteInt(uint8_t *Buffer, int32_t Offset, int32_t Value)
{
	Buffer[Offset++] = Value & 0xFF;
	Buffer[Offset++] = Value >> 8 & 0xFF;
	Buffer[Offset++] = Value >> 16 & 0xFF;
	Buffer[Offset] = Value >> 24 & 0xFF;
}

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
	PyObject *InByteArray;
	if (!PyArg_ParseTuple(args, "Y", &InByteArray))
		return NULL;

	uint8_t *InBuf;
	InBuf = PyByteArray_AsString(InByteArray);
	if (!InBuf)
		return NULL;

	int32_t InSize = (uint32_t)PyByteArray_Size(InByteArray);
	int32_t MaxSize = InSize + (uint32_t)ceil(InSize / 8.0) + (InSize % 8);

	uint8_t *OuBuf;
	OuBuf = (uint8_t *)calloc(MaxSize, sizeof(uint8_t));
	if (!OuBuf)
		return PyErr_NoMemory();

	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OuBuf, MaxSize);
	free(OuBuf);
	return OuByteArray;
}

static PyObject *LZSS_decompress(PyObject *self, PyObject *args)
{
	PyObject *InByteArray;
	uint32_t OuSize;
	if (!PyArg_ParseTuple(args, "YI", &InByteArray, &OuSize))
		return NULL;

	uint8_t *InBuf;
	InBuf = PyByteArray_AsString(InByteArray);
	if (!InBuf)
		return NULL;

	uint8_t *OuBuf;
	OuBuf = (uint8_t *)calloc(OuSize, sizeof(uint8_t));
	if (!OuBuf)
		return PyErr_NoMemory();

	uint32_t InSize = (uint32_t)PyByteArray_Size(InByteArray);
	uint32_t RdCur = 0;
	uint32_t WrCur = 0;
	uint8_t ZipCnt = 0;
	int16_t ZipIdx = 0;

	while (RdCur < InSize)
	{
		uint8_t Flags = InBuf[RdCur++];
		for (int flag_bit = 0; flag_bit < 8; flag_bit++)
		{
			if (Flags & (1 << flag_bit))
				OuBuf[WrCur++] = InBuf[RdCur++];
			else
			{
				ZipCnt = (InBuf[RdCur + 1] & 0xF) + MAXEXPAND - 0xF;
				ZipIdx = (InBuf[RdCur + 1] & 0xF0) * 0x10 + InBuf[RdCur] + MAXEXPAND & 0xFFF;
				if ((uint16_t)ZipIdx > WrCur)
					ZipIdx -= 0x1000;

				for (int zip_idx = 0; zip_idx < ZipCnt; ++zip_idx)
				{
					if (ZipIdx >= 0)
						OuBuf[WrCur++] = OuBuf[ZipIdx++];
					else
					{
						OuBuf[WrCur++] = 0;
						ZipIdx++;
					}
				}
				RdCur += 2;
			}
			if (WrCur >= OuSize)
				break;
		}
	}

	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OuBuf, OuSize);
	free(OuBuf);
	return OuByteArray;
}

static PyMethodDef LZSSMethods[] =
	{
		{"compress", LZSS_compress, METH_VARARGS, NULL},
		{"decompress", LZSS_decompress, METH_VARARGS, NULL},
		{NULL, NULL, 0, NULL} // Sentinel
};

static struct PyModuleDef LZSS_module =
	{
		PyModuleDef_HEAD_INIT,
		"LZSS", // Module name
		NULL,	// Documentation
		-1,		// Size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
		LZSSMethods};

PyMODINIT_FUNC PyInit_LZSS(void)
{
	PyObject *module;

	module = PyModule_Create(&LZSS_module);
	if (module == NULL)
	{
		return NULL;
	}

	return module;
}
