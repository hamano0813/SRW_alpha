#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define MAXEXPAND 0x12

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
    // 读取待压缩的bytearray
	PyObject *InByteArray;
	if (!PyArg_ParseTuple(args, "Y", &InByteArray))
		return NULL;

    // 将输入bytearray转换成字节数组
	uint8_t *InBuf;
	InBuf = PyByteArray_AsString(InByteArray);
	if (!InBuf)
		return NULL;

    // 计算输入bytearray大小并按可能的最大空间需求申请输出bytearray内存空间
	int32_t InSize = (uint32_t)PyByteArray_Size(InByteArray);
	int32_t MaxSize = InSize + (uint32_t)ceil(InSize / 8.0) + (InSize % 8);
	uint8_t *OuBuf;
	OuBuf = (uint8_t *)calloc(MaxSize, sizeof(uint8_t));
	if (!OuBuf)
		return PyErr_NoMemory();

    // 将压缩完毕字节数组转为bytearray并释放申请的内存空间
	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OuBuf, MaxSize);
	free(OuBuf);

	return OuByteArray;
}

static PyObject *LZSS_decompress(PyObject *self, PyObject *args)
{
    // 读取待解压bytearray和输出bytearray大小
	PyObject *InByteArray;
	uint32_t OuSize;
	if (!PyArg_ParseTuple(args, "YI", &InByteArray, &OuSize))
		return NULL;

    // 将输入bytearray转换成字节数组
	uint8_t *InBuf;
	InBuf = PyByteArray_AsString(InByteArray);
	if (!InBuf)
		return NULL;

    // 计算输入bytearray大小并申请输出bytearray内存空间
    uint32_t InSize = (uint32_t)PyByteArray_Size(InByteArray);
	uint8_t *OuBuf;
	OuBuf = (uint8_t *)calloc(OuSize, sizeof(uint8_t));
	if (!OuBuf)
		return PyErr_NoMemory();

    // 初始化解压所需参数
	uint32_t RdCur = 0;
	uint32_t WrCur = 0;
	uint8_t ZipCnt;
	int16_t ZipIdx;

    // 开始解压
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
						OuBuf[WrCur++] = OuBuf[ZipIdx];
					else
						OuBuf[WrCur++] = 0;
					ZipIdx++;
				}
				RdCur += 2;
			}
			if (WrCur >= OuSize)
				break;
		}
	}

    // 将解压完毕字节数组转为bytearray并释放申请的内存空间
	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OuBuf, OuSize);
	free(OuBuf);

	return OuByteArray;
}

static PyMethodDef LZSSMethods[] =
	{
		{"compress", LZSS_compress, METH_VARARGS, "compress data"},
		{"decompress", LZSS_decompress, METH_VARARGS, "decompress data"},
		{NULL, NULL, 0, NULL}
};

static struct PyModuleDef LZSS_module =
	{
		PyModuleDef_HEAD_INIT,
		"LZSS",
		"スパロボ大戦α LZSS-like Comprssion",
		-1,
		LZSSMethods};

PyMODINIT_FUNC PyInit_LZSS(void)
{
	PyObject *module;
	module = PyModule_Create(&LZSS_module);
	if (module == NULL)
		return NULL;
	return module;
}
