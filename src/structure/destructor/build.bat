python build.py build_ext --inplace

DEL /Q LZSS.pyd
REN LZSS.cp310-win_amd64.pyd LZSS.pyd

DEL /Q SNMSG.pyd
REN SNMSG.cp310-win_amd64.pyd SNMSG.pyd

RMDIR /S /Q build
