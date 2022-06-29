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
#include <math.h>
#define SIZEPOS 0
#define DATAPOS 8
#define MAXEXPAND 18
#define BLOCKLENGTH 8

uint32_t ReadInt(uint8_t *Buffer, uint32_t Offset)
{
    uint32_t Value;
    Value = Buffer[Offset++];
    Value += Buffer[Offset++] << 8;
    Value += Buffer[Offset++] << 16;
    Value += Buffer[Offset] << 24;
    return Value;
}

void WriteInt(uint8_t *Buffer, uint32_t Offset, uint32_t Value)
{
    Buffer[Offset++] = Value & 0xFF;
    Buffer[Offset++] = Value >> 8 & 0xFF;
    Buffer[Offset++] = Value >> 16 & 0xFF;
    Buffer[Offset] = Value >> 24 & 0xFF;
}

uint8_t *compress(uint8_t *InputBuffer, uint32_t InputSize)
{
    int WritePos;
    WritePos = DATAPOS;

    int MaxOutputSize;
    MaxOutputSize = InputSize + ceil(InputSize / 8.0) + DATAPOS;

    uint8_t *OutputBuffer;
    OutputBuffer = (uint8_t *)calloc(MaxOutputSize, sizeof(uint8_t));

    WriteInt(OutputBuffer, SIZEPOS, InputSize);

    int BasicPos; //num7
    BasicPos = 8;

    int index;
    int num4;
    
    for (int ReadPos = 0; ReadPos < InputSize; ReadPos++)
    {
        if (BasicPos == 8)
        {
            index = WritePos++;
            OutputBuffer[index] = 0;
            BasicPos = 0;
        }
        int num2;
        num2 = (((ReadPos + 0xfee) / 0x1000) * 0x1000) - 0xfee;
        int num8, num9;
        num8 = 0;
        num9 = 0;
        for (int j = ReadPos - 1; j >= (ReadPos - 0xfff); j--)
        {
            int num5;
            num5 = 0;
            while (num5 < 0x12)
            {
                num4 = 0;
                if ((j + num5) >= 0)
                {
                    num4 = InputBuffer[j + num5];
                }
                if (((ReadPos + num5) == InputSize) || (InputBuffer[ReadPos + num5] != num4))
                {
                    break;
                }
                num5++;
            }
            if (num5 > num8)
            {
                num9 = j - num2;
                if (num9 < 0)
                {
                    num9 += 0x1000;
                }
                num8 = num5;
                if (num8 == 0x12)
                {
                    break;
                }
            }
            if ((ReadPos + num5) == InputSize)
            {
                break;
            }
        }
        OutputBuffer[index] /= 2;
        BasicPos++;
        if (num8 > 2)
        {
            OutputBuffer[WritePos++] = (num9 % 0x100);
            OutputBuffer[WritePos++] = ((((num9 / 0x100) * 0x10) + num8) - 3);
            BasicPos = (BasicPos + num8) - 1;
        }
        else
        {
            OutputBuffer[index] += 0x80;
            OutputBuffer[WritePos++] = InputBuffer[ReadPos];
        }
    }
    for (num4 = 1; num4 <= (8-BasicPos); num4++)
    {
        OutputBuffer[index] /= 2;
    }
    return OutputBuffer;
}

uint8_t *decompress(uint8_t *InputBuffer)
{
    uint32_t ReadPos, WritePos;
    ReadPos = DATAPOS;
    WritePos = 0;

    uint32_t OutputSize;
    OutputSize = ReadInt(InputBuffer, SIZEPOS);

    uint8_t *OutputBuffer;
    OutputBuffer = (uint8_t *)calloc(OutputSize, sizeof(uint8_t));

    int16_t ExpandPos;
    uint8_t ExpandLength;

    while (1)
    {
        uint8_t BasicFlag;
        BasicFlag = InputBuffer[ReadPos++];

        for (int BasicIdx = 0; BasicIdx < BLOCKLENGTH; BasicIdx++)
        {
            if (BasicFlag & (1 << BasicIdx))
                OutputBuffer[WritePos++] = InputBuffer[ReadPos++];
            else
            {
                ExpandLength = (InputBuffer[ReadPos + 1] & 0xF) + MAXEXPAND - 0xF;
                ExpandPos = (InputBuffer[ReadPos + 1] & 0xF0) * 0x10 + InputBuffer[ReadPos] + MAXEXPAND & 0xFFF;
                if (ExpandPos > WritePos)
                    ExpandPos -= 0x1000;

                for (int ExpandIdx = 0; ExpandIdx < ExpandLength; ++ExpandIdx)
                {
                    if (ExpandPos < 0)
                        OutputBuffer[WritePos++] = 0;
                    else
                        OutputBuffer[WritePos++] = OutputBuffer[ExpandPos];
                    ExpandPos++;
                }
                ReadPos += 2;
            }
            if (WritePos >= OutputSize)
                return OutputBuffer;
        }
    }
}
