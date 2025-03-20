from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

lxml_binaries = collect_dynamic_libs('lxml')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=lxml_binaries,
    datas=[('nazwa_bazy.db', '.',),('json-styles/style.json', 'json-styles')],
    hiddenimports=['PySide6'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'PySide2', 'PyQt6'],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FirenetViewer',
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
    onefile=True
)

