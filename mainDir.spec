from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

lxml_binaries = collect_dynamic_libs('lxml')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=lxml_binaries,
    datas=[('json-styles/style.json', 'json-styles'),('Qss/*', 'Qss'),('fonts', 'fonts'),('generated-files/*', 'generated-files')],
    hiddenimports=['PySide6','openpyxl','openpyxl.cell._writer'],
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
    exclude_binaries=False,
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
	onefile=True,
)


coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)