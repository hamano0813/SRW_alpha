#define PY_SSIZE_T_CLEAN
#include <Python.h>

#define THRESHOLD 2
#define PBIT 4
#define WBIT 12
#define PSIZE (1 << PBIT)
#define WSIZE (1 << WBIT)
#define BSIZE (WSIZE - PSIZE - THRESHOLD)
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

int adj_cur(unsigned char *buf, int r_cur, int cur, char cnt)
{
	for (char idx = 0; idx < cnt; idx++)
		if (buf[r_cur + idx] != 0)
			return max(BSIZE - idx, cur);
	return cur;
}

int find_match(unsigned char *buf, int r_cur, int cur, char cnt)
{
	cur = adj_cur(buf, r_cur, cur, cnt);
	for (; cur < r_cur; cur++)
	{
		char idx = 0;
		for (; idx < cnt; idx++)
			if (buf[cur + idx] != buf[r_cur + idx])
				break;
		if (idx == cnt)
			return cur;
	}
	return -1;
}

static PyObject *LZSS_compress(PyObject *self, PyObject *args)
{
	PyObject *InByte;
	if (!PyArg_ParseTuple(args, "Y", &InByte))
		return NULL;

	const int i_size = (int)PyByteArray_Size(InByte);
	const int m_size = HEAD + i_size + i_size / CHAR_BIT + 1;

	unsigned char temp[BSIZE] = {0};
	PyObject *TempByte = PyByteArray_FromStringAndSize(temp, BSIZE);
	PyObject *RdByte = PyByteArray_Concat(TempByte, InByte);

	unsigned char *r_buf = PyByteArray_AsString(RdByte);
	const int r_size = (int)PyByteArray_Size(RdByte);
	char *w_buf = (char *)calloc(m_size, sizeof(char));
	write_size(w_buf, i_size);

	char f_bit = CHAR_BIT;
	int f_cur = 0;
	int r_cur = BSIZE;
	int w_cur = HEAD;

	while (r_cur < r_size)
	{
		if (f_bit == CHAR_BIT)
		{
			f_cur = w_cur++;
			f_bit = 0;
		}
		char m_cnt = THRESHOLD;
		int m_cur = 0;

		int cur = min(r_cur - BSIZE, i_size - PSIZE - THRESHOLD);
		for (char cnt = PSIZE + THRESHOLD; cnt > THRESHOLD; cnt--)
		{
			if (r_cur + cnt <= r_size)
				m_cur = find_match(r_buf, r_cur, cur, cnt);
			if (m_cur > 0)
			{
				m_cnt = cnt;
				break;
			}
		}

		if (m_cnt > THRESHOLD)
		{
			w_buf[w_cur++] = m_cur & 0xFF;
			w_buf[w_cur++] = (m_cur >> 4 & 0xF0 | m_cnt - THRESHOLD - 1);
			r_cur += m_cnt;
		}
		else
		{
			w_buf[w_cur++] = r_buf[r_cur++];
			w_buf[f_cur] |= 1 << f_bit;
		}
		f_bit++;
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
	const unsigned int r_size = (unsigned int)PyByteArray_Size(InByte);
	const unsigned int w_size = read_size(r_buf);
	unsigned char *w_buf = (unsigned char *)calloc(max(w_size, WSIZE), sizeof(unsigned char));

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
				/*if (m_cur > (short)w_cur)
					m_cur -= WSIZE;*/

				for (char m_idx = 0; m_idx < m_cnt; m_idx++, m_cur++)
				{
					/*if (m_cur < 0)
						w_buf[w_cur++] = 0;
					else*/
					w_buf[w_cur++] = w_buf[(unsigned short)m_cur & (WSIZE - 1)];
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
		"LZSS compression algorithm for スパロボット大戦α",
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
