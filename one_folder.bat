title build SRW�� project
python -m venv venv --upgrade-deps
call venv/scripts/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
python release.py src/SRW��.pyw
pyinstaller one_folder.spec
RMDIR /S /Q release
RMDIR /S /Q build
RMDIR /S /Q venv
RMDIR /S /Q dist\SRW��\PySide6\translations
pause