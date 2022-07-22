#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define THRESHOLD 2
#define PBIT 4
#define WBIT 12
#define PSIZE (1 << PBIT)
#define WSIZE (1 << WBIT)
#define HEAD 8

unsigned int read_size(unsigned char *buf)
{
	return (unsigned int)(buf[0] | buf[1] << 8 | buf[2] << 16 | buf[3] << 24);
}
void write_size(unsigned char *buf, unsigned int size)
{
	buf[0] = size & 0xFF;
	buf[1] = (size >> 8) & 0xFF;
	buf[2] = (size >> 16) & 0xFF;
	buf[3] = (size >> 24) & 0xFF;
}

#define CHAR unsigned char
#define BYTE char
#define WORD short
#define DOUBLE int

#define MAXSIZE 0x8000
#define PREBUFBIT 4
#define WINBUFBIT 12

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
	PyObject *InByte;
	if (!PyArg_ParseTuple(args, "Y", &InByte))
		return NULL;

	unsigned char *i_buf = PyByteArray_AsString(InByte);
	const unsigned int i_size = (unsigned int)PyByteArray_Size(InByte);
	const unsigned int m_size = HEAD + i_size + i_size / 8 + 1;
	unsigned char *w_buf = (unsigned char *)calloc(m_size, sizeof(unsigned char));

	short f_cur;
	short w_cur = 8;
	char f_idx = 8;

	write_size(w_buf, i_size);
	for (short r_cur = 0; r_cur < i_size; r_cur++)
	{
		if (f_idx == 8)
		{
			f_cur = w_cur++;
			f_idx = 0;
		}
		char m_cnt = THRESHOLD;
		int m_cur;
		for (short p_idx = r_cur - 1; p_idx > (short)max((r_cur - WSIZE), 0); p_idx--)
		{
			char m_idx = 0;
			for (m_idx; m_idx < (PSIZE + 2); m_idx++)
			{
				char m_val = 0;
				if ((p_idx + m_idx) >= 0)
					m_val = i_buf[p_idx + m_idx];
				if (((r_cur + m_idx) == i_size) || (i_buf[r_cur + m_idx] != m_val))
					break;
			}
			if (m_idx > m_cnt)
			{
				m_cur = p_idx - PSIZE - THRESHOLD & 0xFFF;
				m_cnt = m_idx;
				if (m_cnt == (PSIZE + THRESHOLD))
					break;
			}
			if ((r_cur + m_idx) == i_size)
				break;
		}
		f_idx++;
		if (m_cnt > THRESHOLD)
		{
			w_buf[w_cur++] = m_cur & ((1 << CHAR_BIT) - 1);
			w_buf[w_cur++] = m_cur >> CHAR_BIT << PBIT | (m_cnt - THRESHOLD - 1);
			r_cur = (r_cur + m_cnt) - 1;
		}
		else
		{
			w_buf[f_cur] |= (1 << (f_idx - 1));
			w_buf[w_cur++] = i_buf[r_cur];
		}
	}

	PyObject *OutByte = PyByteArray_FromStringAndSize(w_buf, w_cur);
	free(w_buf);

	return OutByte;
}

static PyObject *LZSS_decompress(PyObject *self, PyObject *args)
{
	PyObject *InByte;
	if (!PyArg_ParseTuple(args, "Y", &InByte))
		return NULL;

	unsigned char *r_buf = PyByteArray_AsString(InByte);
	const unsigned int r_size = (size_t)PyByteArray_Size(InByte);
	const unsigned int w_size = read_size(r_buf);
	unsigned char *w_buf = (unsigned char *)calloc(w_size, sizeof(unsigned char));

	unsigned int r_cur = 8;
	unsigned int w_cur = 0;

	while (r_cur < r_size)
	{
		char f_bits = r_buf[r_cur++];
		for (char f_idx = 0; f_idx < CHAR_BIT; f_idx++)
		{
			if (f_bits & (1 << f_idx))
				w_buf[w_cur++] = r_buf[r_cur++];
			else
			{
				char m_cnt = (r_buf[r_cur + 1] & (PSIZE - 1)) + THRESHOLD + 1;
				short m_cur = (r_buf[r_cur + 1] >> PBIT << CHAR_BIT | r_buf[r_cur]) + PSIZE + THRESHOLD & (WSIZE - 1);
				if (m_cur > w_cur)
					m_cur -= WSIZE;

				for (char m_idx = 0; m_idx < m_cnt; m_idx++, m_cur++)
				{
					if (m_cur < 0)
						w_buf[w_cur++] = 0;
					else
						w_buf[w_cur++] = w_buf[m_cur];
				}
				r_cur += 2;
			}
			if (r_cur >= r_size)
				break;
		}
	}
	PyObject *OutByte = PyByteArray_FromStringAndSize(w_buf, w_size);
	free(w_buf);
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
