#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define FLAGWIDTH 8
#define THRESHOLD 2

uint8_t GetPreBits(uint8_t *Buffer, uint32_t Offset)
{
	return Buffer[Offset + 1] & (1 << 4) - 1;
}
uint16_t GetFwdBits(uint8_t *Buffer, uint32_t Offset)
{
	return (Buffer[Offset + 1] >> 4 << 8) | Buffer[Offset];
}

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
	// 读取待压缩的bytearray
	PyObject *InByteArray;
	if (!PyArg_ParseTuple(args, "Y", &InByteArray))
		return NULL;

	// 将输入bytearray转换成字节数组
	uint8_t *InBuffer;
	InBuffer = PyByteArray_AsString(InByteArray);
	if (!InBuffer)
		return NULL;

	// 计算输入bytearray大小并按可能的最大空间需求申请输出bytearray内存空间
	uint32_t InSize = (uint32_t)PyByteArray_Size(InByteArray);
	uint32_t MaxSize = InSize + (uint32_t)ceil(InSize / 8.0) + (InSize % 8);
	uint8_t *OutBuffer;
	OutBuffer = (uint8_t *)calloc(MaxSize, sizeof(uint8_t));
	if (!OutBuffer)
		return PyErr_NoMemory();

	uint32_t MatchValue;
	uint32_t FlagsOffset;
	uint32_t WriteOffset = 0;
	uint32_t FlagBit = 8;

	for (int ReadOffset = 0; ReadOffset < (int)InSize; ReadOffset++)
	{
		if (FlagBit == 8)
		{
			FlagsOffset = WriteOffset++;
			OutBuffer[FlagsOffset] = 0;
			FlagBit = 0;
		}
		int16_t ReadFlag = (((ReadOffset + 0xfee) / 0x1000) * 0x1000) - 0xfee;
		int8_t MatchCount = 0;
		int16_t MatchOffset = 0;
		for (int PreIndex = ReadOffset - 1; PreIndex >= (ReadOffset - 0xFFF); PreIndex--)
		{
			int FwdIndex = 0;
			while (FwdIndex <= 0x11)
			{
				MatchValue = 0;
				if ((PreIndex + FwdIndex) >= 0)
					MatchValue = InBuffer[PreIndex + FwdIndex];
				if ((ReadOffset + FwdIndex) == InSize)
					break;
				if (InBuffer[ReadOffset + FwdIndex] != MatchValue)
					break;
				FwdIndex++;
			}

			if (FwdIndex > MatchCount)
			{
				MatchOffset = PreIndex - ReadFlag;

				if (MatchOffset < 0)
				{
					MatchOffset += 0x1000;
				}
				MatchCount = FwdIndex;
				if (MatchCount == 0x12)
				{
					break;
				}
			}
			if ((ReadOffset + FwdIndex) == InSize)
			{
				break;
			}
		}

		OutBuffer[FlagsOffset] = (int8_t)(OutBuffer[FlagsOffset] / 2);
		FlagBit++;
		if (MatchCount > 2)
		{
			// printf("%X\t%X\t%X\n", MatchOffset, MatchCount, num2);
			OutBuffer[WriteOffset] = (uint8_t)(MatchOffset % 0x100);
			WriteOffset++;
			OutBuffer[WriteOffset] = (uint8_t)((((MatchOffset / 0x100) * 0x10) + MatchCount) - 3);
			WriteOffset++;
			ReadOffset = (ReadOffset + MatchCount) - 1;
		}
		else
		{
			OutBuffer[FlagsOffset] = (int8_t)(OutBuffer[FlagsOffset] + 0x80);
			OutBuffer[WriteOffset] = InBuffer[ReadOffset];
			WriteOffset++;
		}
	}
	for (MatchValue = 1; MatchValue <= (8 - FlagBit); MatchValue++)
	{
		OutBuffer[FlagsOffset] = (int8_t)(OutBuffer[FlagsOffset] / 2);
	}

	// 将压缩完毕字节数组转为bytearray并释放申请的内存空间
	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OutBuffer, WriteOffset);
	free(OutBuffer);

	return OuByteArray;
}

static PyObject *LZSS_decompress(PyObject *self, PyObject *args)
{
	PyObject *InByteArray;
	uint32_t OutSize;
	if (!PyArg_ParseTuple(args, "YI", &InByteArray, &OutSize))
		return NULL;

	uint8_t *InBuffer;
	InBuffer = PyByteArray_AsString(InByteArray);
	if (!InBuffer)
		return NULL;

	uint8_t *OutBuffer;
	OutBuffer = (uint8_t *)calloc(OutSize, sizeof(uint8_t));
	if (!OutBuffer)
		return PyErr_NoMemory();

	uint32_t ReadOffset = 0;
	uint32_t WriteOffset = 0;
	uint8_t MatchCount;
	int16_t MatchOffset;

	while (WriteOffset < OutSize)
	{
		uint8_t Flags = InBuffer[ReadOffset++];
		for (int FlagBit = 0; FlagBit < FLAGWIDTH; FlagBit++)
		{
			if (Flags & (1 << FlagBit))
				OutBuffer[WriteOffset++] = InBuffer[ReadOffset++];
			else
			{
				MatchCount = GetPreBits(InBuffer, ReadOffset) + THRESHOLD + 1;
				MatchOffset = GetFwdBits(InBuffer, ReadOffset) + THRESHOLD + 0x10 & 0xFFF;

				if ((uint16_t)MatchOffset > WriteOffset)
					MatchOffset -= 0x1000;

				for (int MatchIndex = 0; MatchIndex < MatchCount; MatchIndex++, MatchOffset++)
				{
					if (MatchOffset < 0)
						OutBuffer[WriteOffset++] = 0;
					else
						OutBuffer[WriteOffset++] = OutBuffer[MatchOffset];
				}
				ReadOffset += 2;
			}
			if (WriteOffset >= OutSize)
				break;
		}
	}

	PyObject *OutByteArray = PyByteArray_FromStringAndSize(OutBuffer, OutSize);
	free(OutBuffer);

	return OutByteArray;
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
