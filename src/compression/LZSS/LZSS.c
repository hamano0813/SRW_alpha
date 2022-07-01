#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define MAXMATCH 0x12

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
	uint32_t InSize = (uint32_t)PyByteArray_Size(InByteArray);
	uint32_t MaxSize = InSize + (uint32_t)ceil(InSize / 8.0) + (InSize % 8);
	uint8_t *OuBuf;
	OuBuf = (uint8_t *)calloc(MaxSize, sizeof(uint8_t));
	if (!OuBuf)
		return PyErr_NoMemory();

	uint32_t MVal;
	uint32_t FlagsCur;
	uint32_t WrCur = 0;
	uint32_t BlkCnt = 8;

	for (uint32_t RdCur = 0; RdCur < InSize; RdCur++)
	{
		if (BlkCnt == 8)
		{
			FlagsCur = WrCur++;
			OuBuf[FlagsCur] = 0;
			BlkCnt = 0;
		}
		int num2 = (((RdCur + 0xfee) / 0x1000) * 0x1000) - 0xfee;
		int ZipCnt = 0;
		int ZipIdx = 0;
		for (int m_cur = RdCur - 1; m_cur > ((int32_t)RdCur - 0x1000); m_cur--)
		{
			int MCtn = 0;
			while (MCtn < MAXMATCH)
			{
				MVal = 0;
				if ((m_cur + MCtn) >= 0)
				{
					MVal = InBuf[m_cur + MCtn];
				}
				if (((RdCur + MCtn) == InSize) || (InBuf[RdCur + MCtn] != MVal))
				{
					break;
				}
				MCtn++;
			}
			if (MCtn > ZipCnt)
			{
				ZipIdx = m_cur - num2;
				if (ZipIdx < 0)
				{
					ZipIdx += 0x1000;
				}
				ZipCnt = MCtn;
				if (ZipCnt == 0x12)
				{
					break;
				}
			}
			if ((RdCur + MCtn) == InSize)
			{
				break;
			}
		}
		OuBuf[FlagsCur] = (int8_t)(OuBuf[FlagsCur] / 2);
		BlkCnt++;
		if (ZipCnt > 2)
		{
			OuBuf[WrCur] = (int8_t)(ZipIdx % 0x100);
			WrCur++;
			OuBuf[WrCur] = (int8_t)((((ZipIdx / 0x100) * 0x10) + ZipCnt) - 3);
			WrCur++;
			RdCur = (RdCur + ZipCnt) - 1;
		}
		else
		{
			OuBuf[FlagsCur] = (int8_t)(OuBuf[FlagsCur] + 0x80);
			OuBuf[WrCur] = InBuf[RdCur];
			WrCur++;
		}
	}
	for (MVal = 1; MVal <= (8 - BlkCnt); MVal++)
	{
		OuBuf[FlagsCur] = (int8_t)(OuBuf[FlagsCur] / 2);
	}

	// 将压缩完毕字节数组转为bytearray并释放申请的内存空间
	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OuBuf, WrCur);
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
				ZipCnt = (InBuf[RdCur + 1] & 0xF) + MAXMATCH - 0xF;
				ZipIdx = (InBuf[RdCur + 1] & 0xF0) * 0x10 + InBuf[RdCur] + MAXMATCH & 0xFFF;
				if ((uint16_t)ZipIdx > WrCur)
					ZipIdx -= 0x1000;

				for (int zip_idx = 0; zip_idx < ZipCnt; ++zip_idx)
				{
					if (ZipIdx < 0)
						OuBuf[WrCur++] = 0;
					else
						OuBuf[WrCur++] = OuBuf[ZipIdx];
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
		{NULL, NULL, 0, NULL}};

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
