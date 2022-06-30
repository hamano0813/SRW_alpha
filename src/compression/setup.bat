python setup.py build_ext --inplace
DEL /Q LZSS.pyd
REN LZSS.cp310-win_amd64.pyd LZSS.pyd
RMDIR /S /Q build
