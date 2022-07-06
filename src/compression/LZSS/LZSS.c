#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define BYTE unsigned char
#define WORD short
#define DWORD int

#define MAXSIZE 0x8000
#define THRESHOLD 2
#define PREBUFBIT 4
#define WINBUFBIT 12

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
	PyObject *InByteArray;
	if (!PyArg_ParseTuple(args, "Y", &InByteArray))
		return NULL;
	BYTE *InBuffer;
	InBuffer = PyByteArray_AsString(InByteArray);
	if (!InBuffer)
		return NULL;
	BYTE *OutBuf;
	OutBuf = (BYTE *)calloc(MAXSIZE, sizeof(BYTE));
	if (!OutBuf)
		return PyErr_NoMemory();

	const BYTE PreSize = (1 << PREBUFBIT);
	const WORD WinSize = (1 << WINBUFBIT);
	const DWORD RdSize = (DWORD)PyByteArray_Size(InByteArray);

	DWORD FlagCur;
	DWORD WrCur = 0;
	BYTE FlagBit = 8;

	for (DWORD RdCur = 0; RdCur < RdSize; RdCur++)
	{
		if (FlagBit == 8)
		{
			FlagCur = WrCur++;
			OutBuf[FlagCur] = 0;
			FlagBit = 0;
		}
		WORD matchAdj = (((RdCur + 0xFEE) / WinSize) * WinSize) - 0xFEE;
		BYTE matchCnt = 0;
		WORD matchCur = 0;
		for (DWORD pre_idx = RdCur - 1; pre_idx > (DWORD)max((RdCur - WinSize), (-PreSize - THRESHOLD)); pre_idx--)
		{
			BYTE match_idx = 0;
			for (match_idx; match_idx < (PreSize + 2); match_idx++)
			{
				BYTE matchVal = 0;
				if ((pre_idx + match_idx) >= 0)
					matchVal = InBuffer[pre_idx + match_idx];
				if (((RdCur + match_idx) == RdSize) || (InBuffer[RdCur + match_idx] != matchVal))
					break;
			}
			if (match_idx > matchCnt)
			{
				matchCur = pre_idx - matchAdj;
				if (matchCur < 0)
					matchCur += WinSize;
				matchCnt = match_idx;
				if (matchCnt == (PreSize + THRESHOLD))
					break;
			}
			if ((RdCur + match_idx) == RdSize)
				break;
		}

		FlagBit++;
		if (matchCnt > THRESHOLD)
		{
			OutBuf[WrCur++] = (BYTE)(matchCur & 0xFF);
			OutBuf[WrCur++] = (BYTE)(((matchCur / 0x100) * 0x10) + matchCnt - 3);
			RdCur = (RdCur + matchCnt) - 1;
		}
		else
		{
			OutBuf[FlagCur] |= (1 << (FlagBit - 1));
			OutBuf[WrCur++] = InBuffer[RdCur];
		}
	}

	PyObject *OuByteArray = PyByteArray_FromStringAndSize(OutBuf, WrCur);
	free(OutBuf);

	return OuByteArray;
}

static PyObject *LZSS_decompress(PyObject *self, PyObject *args)
{
	PyObject *InByteArray;
	if (!PyArg_ParseTuple(args, "Y", &InByteArray))
		return NULL;
	BYTE *InBuf;
	InBuf = PyByteArray_AsString(InByteArray);
	if (!InBuf)
		return NULL;
	BYTE *OutBuf;
	OutBuf = (BYTE *)calloc(MAXSIZE, sizeof(BYTE));
	if (!OutBuf)
		return PyErr_NoMemory();

	const BYTE PreSize = (1 << PREBUFBIT);
	const WORD WinSize = (1 << WINBUFBIT);
	const DWORD RdSize = (DWORD)PyByteArray_Size(InByteArray);
	DWORD RdCur = 0;
	DWORD WrCur = 0;

	while (RdCur < RdSize)
	{
		BYTE flagBits = InBuf[RdCur++];
		for (BYTE bit_idx = 0; bit_idx < CHAR_BIT; bit_idx++)
		{
			if (flagBits & (1 << bit_idx))
				OutBuf[WrCur++] = InBuf[RdCur++];
			else
			{
				BYTE matchCnt = (InBuf[RdCur + 1] & (PreSize - 1)) + 1 + THRESHOLD;
				WORD matchCur = (InBuf[RdCur + 1] >> PREBUFBIT << CHAR_BIT | InBuf[RdCur]) + PreSize + THRESHOLD & (WinSize - 1);
				if (matchCur > WrCur)
					matchCur -= WinSize;

				for (int match_idx = 0; match_idx < matchCnt; match_idx++, matchCur++)
				{
					if (matchCur < 0)
						OutBuf[WrCur++] = 0;
					else
						OutBuf[WrCur++] = OutBuf[matchCur];
				}
				RdCur += 2;
			}
			if (RdCur >= RdSize)
				break;
		}
	}
	PyObject *OutByteArray = PyByteArray_FromStringAndSize(OutBuf, WrCur);
	free(OutBuf);
	return OutByteArray;
}

static PyMethodDef LZSSMethods[] =
	{
		{"compress", LZSS_compress, METH_VARARGS, "use the LZSS algorithm to compress data."},
		{"decompress", LZSS_decompress, METH_VARARGS, "use the LZSS algorithm to decompress data."},
		{NULL, NULL, 0, NULL}};

static struct PyModuleDef LZSS_module =
	{
		PyModuleDef_HEAD_INIT,
		"LZSS",
		"special LZSS compression algorithm for スパロボット大戦α",
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
