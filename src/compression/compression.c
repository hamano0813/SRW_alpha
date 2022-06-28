/*
用于解压和压缩机战α数据的C函数

编译DLL
gcc compression.c -shared -o compression.dll

python中调用
from ctypes import CDLL, POINTER, byref, c_ubyte

o_buffer: bytes | bytearray
size = len(o_buffer)
c_buf = (c_ubyte * size)(*buffer)

compression = CDLL('./compression')
compression.decompress.restype = POINTER(c_ubyte)
compression.compress.restype = POINTER(c_ubyte)

p_buffer = compression.compress(byref(c_buf), size)
p_buffer = compression.decompress(byref(c_buf))

t_buffer = bytes(p_buffer[:size])
*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#define SIZEPOS 0
#define MAXEXPAND 18
#define BASICLENGTH 8

unsigned int ReadInt(unsigned char *Buffer, unsigned int Offset) //读取无符号整数
{
    int Value;
    Value = Buffer[Offset++];
    Value += Buffer[Offset++] << 8;
    Value += Buffer[Offset++] << 16;
    Value += Buffer[Offset] << 24;
    return Value;
}

void WriteInt(unsigned char *Buffer, unsigned int Offset, unsigned int Value) //写入无符号整数
{
    Buffer[Offset++] = Value & 0xFF;
    Buffer[Offset++] = Value >> 8 & 0xFF;
    Buffer[Offset++] = Value >> 16 & 0xFF;
    Buffer[Offset] = Value >> 24 & 0xFF;
}

unsigned char *compress(unsigned char *InputBuffer, unsigned int OutputSize) // 压缩数据
{
    unsigned int ReadPos, WritePos; // 定义读写下标并初始化
    ReadPos = 0;
    WritePos = 8;

    unsigned char *OutputBuffer; // 申请内存空间
    OutputBuffer = (unsigned char *)calloc(OutputSize, sizeof(unsigned char));

    WriteInt(OutputBuffer, SIZEPOS, OutputSize); // 写入原文件大小

    

    return OutputBuffer;
}

unsigned char *decompress(unsigned char *InputBuffer) // 解压数据
{
    unsigned int ReadPos, WritePos; // 定义读写下标并初始化
    ReadPos = 8;
    WritePos = 0;

    unsigned int OutputSize; // 读取原文件大小
    OutputSize = ReadInt(InputBuffer, SIZEPOS);

    unsigned char *OutputBuffer; // 申请内存空间
    OutputBuffer = (unsigned char *)calloc(OutputSize, sizeof(unsigned char));

    while (1)
    {
        int BasicFlag; // 读取1个字节的压缩标识
        BasicFlag = InputBuffer[ReadPos++];

        for (int BasicIdx = 0; BasicIdx < BASICLENGTH; BasicIdx++)
        {
            if (BasicFlag & (1 << BasicIdx))
            {
                OutputBuffer[WritePos++] = InputBuffer[ReadPos++];
            }
            else
            {

                int ExpandPos;
                ExpandPos = (InputBuffer[ReadPos + 1] & 0xF0) * 0x10 + InputBuffer[ReadPos] + MAXEXPAND & 0xFFF;

                int ExpandLength;
                ExpandLength = (InputBuffer[ReadPos + 1] & 0xF) + MAXEXPAND - 0xF;

                if (ExpandPos > WritePos)
                {
                    ExpandPos -= 0x1000;
                }

                for (int ExpandIdx = 0; ExpandIdx < ExpandLength; ++ExpandIdx)
                {
                    if (ExpandPos < 0)
                    {
                        OutputBuffer[WritePos++] = 0;
                    }
                    else
                    {
                        OutputBuffer[WritePos++] = OutputBuffer[ExpandPos];
                    }
                    ExpandPos++;
                }
                ReadPos += 2;
            }
            if (WritePos >= OutputSize)
            {
                return OutputBuffer;
            }
        }
    }
}
