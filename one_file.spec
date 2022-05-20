# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['release\\SRWα.pyw'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

to_keep = []
to_exclude = {
    'opengl32sw.dll',
    'Qt6Network.dll',
    'Qt6OpenGL.dll',
    'Qt6Qml.dll',
    'Qt6QmlModels.dll',
    'Qt6Quick.dll',
    'qwebp.dll',
    'qtiff.dll',
    'qwbmp.dll',
    'qpdf.dll',
    'qnetworklistmanager.dll',
    'qwindowsvistastyle.dll',
    'qcertonlybackend.dll',
    'qopensslbackend.dll',
    'qschannelbackend.dll',
    }

# Iterate through the list of included binaries.
for (dest, source, kind) in a.binaries:
    # Skip anything we don't need.
    if os.path.split(dest)[1] in to_exclude:
        continue
    to_keep.append((dest, source, kind))

# Replace list of data files with filtered one.
a.binaries = to_keep

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SRWα',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
