
from ctypes import CDLL, POINTER, byref, c_ubyte, c_int32
from struct import unpack_from


robot_raf = r'..\..\resource\bin\jp\ROBOT.RAF'
uncompress_robot_raf = r'..\..\resource\bin\jp\UNCOMPRESS_ROBOT.RAF'

with open(robot_raf, 'rb') as f1:
    o_data = bytearray(f1.read())

with open(uncompress_robot_raf, 'rb') as f2:
    n_data = bytearray(f2.read())

count = unpack_from('I', o_data, 0x0)[0]
pointers = list(unpack_from('I' * count, o_data, 0x4))
pointers.append(len(o_data))

offset = (count + 1) * 4

compression = CDLL(r'..\compression\compression')

compression.decompress.restype = POINTER(c_ubyte)
compression.compress.restype = POINTER(c_ubyte)

com_buffer = (c_ubyte * len(n_data))(*bytearray(n_data))
# test = bytearray(compression.compress(byref(com_buffer), c_int32(0x2C4))[:0x2C4])
# print(test)


for i in range(count):
    input_buf = o_data[offset + pointers[i]: offset + pointers[i + 1]]
    input_size = pointers[i + 1] - pointers[i]
    output_size = unpack_from('I', input_buf, 0x0)[0]
    input_buffer = (c_ubyte * input_size)(*input_buf)
    out_buf = bytearray(compression.decompress(byref(input_buffer))[: output_size])
    tes_buf = n_data[output_size * i: output_size * (i + 1)]
    if not out_buf == tes_buf:
        print(i)
