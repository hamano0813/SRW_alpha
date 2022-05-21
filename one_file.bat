title build SRW¦Á project
python -m venv venv --upgrade-deps
call venv/scripts/activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
python release.py src/SRW¦Á.pyw
pyinstaller one_file.spec
RMDIR /S /Q release
RMDIR /S /Q build
RMDIR /S /Q venv
pause