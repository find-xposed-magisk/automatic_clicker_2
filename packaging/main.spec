# -*- mode: python ; coding: utf-8 -*-

import os


project_root = os.path.dirname(os.path.abspath(SPECPATH))


a = Analysis(
    [os.path.join(project_root, 'main.py')],
    pathex=[project_root],
    binaries=[],
    datas=[
        (os.path.join(project_root, 'data', '命令集.db'), 'data'),
        (os.path.join(project_root, 'flat', 'Combinear.qss'), 'flat'),
        (os.path.join(project_root, 'flat', '开屏.png'), 'flat'),
    ],
    hiddenimports=['pyttsx4.drivers'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Clicker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='.',
    uac_admin=True,
    icon=os.path.join(project_root, 'clicker.ico'),
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Clicker',
)
