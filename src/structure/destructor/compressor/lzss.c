#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define CHAR unsigned char
#define BYTE char
#define WORD short
#define DOUBLE int

#define MAXSIZE 0x8000
#define THRESHOLD 2
#define PBIT 4
#define WBIT 12
#define PSIZE (1 << PBIT)
#define WSIZE (1 << WBIT)

unsigned int read_size(unsigned char *buf)
{
	return (unsigned int)(buf[0] | buf[1] << 8 | buf[2] << 16 | buf[3] << 24);
}
void write_size(unsigned char *buf, unsigned int size)
{
	buf[0] = (size >> 24) & 0xFF;
	buf[1] = (size >> 16) & 0xFF;
	buf[2] = (size >> 8) & 0xFF;
	buf[3] = size & 0xFF;
}

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
	PyObject *InByte;
	if (!PyArg_ParseTuple(args, "Y", &InByte))
		return NULL;
	unsigned char *i_buf = PyByteArray_AsString(InByte);
	unsigned char *o_buf = (unsigned char *)calloc(MAXSIZE, sizeof(char));

	const DOUBLE RdSize = (DOUBLE)PyByteArray_Size(InByte);

	DOUBLE FlagCur;
	DOUBLE WrCur = 0;
	BYTE FlagBit = 8;

	for (DOUBLE RdCur = 0; RdCur < RdSize; RdCur++)
	{
		if (FlagBit == 8)
		{
			FlagCur = WrCur++;
			o_buf[FlagCur] = 0;
			FlagBit = 0;
		}
		WORD matchAdj = (((RdCur + 0xFEE) / WSIZE) * WSIZE) - 0xFEE;
		BYTE matchCnt = 0;
		WORD matchCur = 0;
		for (DOUBLE pre_idx = RdCur - 1; pre_idx > (DOUBLE)max((RdCur - WSIZE), (-PSIZE - THRESHOLD)); pre_idx--)
		{
			BYTE match_idx = 0;
			for (match_idx; match_idx < (PSIZE + 2); match_idx++)
			{
				BYTE matchVal = 0;
				if ((pre_idx + match_idx) >= 0)
					matchVal = i_buf[pre_idx + match_idx];
				if (((RdCur + match_idx) == RdSize) || (i_buf[RdCur + match_idx] != matchVal))
					break;
			}
			if (match_idx > matchCnt)
			{
				matchCur = pre_idx - matchAdj;
				if (matchCur < 0)
					matchCur += WSIZE;
				matchCnt = match_idx;
				if (matchCnt == (PSIZE + THRESHOLD))
					break;
			}
			if ((RdCur + match_idx) == RdSize)
				break;
		}

		FlagBit++;
		if (matchCnt > THRESHOLD)
		{
			o_buf[WrCur++] = (BYTE)(matchCur & 0xFF);
			o_buf[WrCur++] = (BYTE)(((matchCur / 0x100) * 0x10) + matchCnt - 3);
			RdCur = (RdCur + matchCnt) - 1;
		}
		else
		{
			o_buf[FlagCur] |= (1 << (FlagBit - 1));
			o_buf[WrCur++] = i_buf[RdCur];
		}
	}

	PyObject *OuByteArray = PyByteArray_FromStringAndSize(o_buf, WrCur);
	free(o_buf);

	return OuByteArray;
}

static PyObject *LZSS_decompress(PyObject *self, PyObject *args)
{
	PyObject *InByte;
	if (!PyArg_ParseTuple(args, "Y", &InByte))
		return NULL;
	unsigned char *i_buf = PyByteArray_AsString(InByte);
	const unsigned int i_size = (size_t)PyByteArray_Size(InByte);
	const unsigned int o_size = read_size(i_buf);
	unsigned char *o_buf = (unsigned char *)calloc(o_size, sizeof(unsigned char));

	unsigned int i_cur = 8;
	unsigned int o_cur = 0;

	while (i_cur < i_size)
	{
		char f_bits = i_buf[i_cur++];
		for (char f_idx = 0; f_idx < CHAR_BIT; f_idx++)
		{
			if (f_bits & (1 << f_idx))
				o_buf[o_cur++] = i_buf[i_cur++];
			else
			{
				char m_cnt = (i_buf[i_cur + 1] & (PSIZE - 1)) + THRESHOLD + 1;
				short m_cur = (i_buf[i_cur + 1] >> PBIT << CHAR_BIT | i_buf[i_cur]) + PSIZE + THRESHOLD & (WSIZE - 1);
				if (m_cur > o_cur)
					m_cur -= WSIZE;

				for (char m_idx = 0; m_idx < m_cnt; m_idx++, m_cur++)
				{
					if (m_cur < 0)
						o_buf[o_cur++] = 0;
					else
						o_buf[o_cur++] = o_buf[m_cur];
				}
				i_cur += 2;
			}
			if (i_cur >= i_size)
				break;
		}
	}
	PyObject *OutByte = PyByteArray_FromStringAndSize(o_buf, o_size);
	free(o_buf);
	return OutByte;
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
