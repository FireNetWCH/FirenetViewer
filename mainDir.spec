from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

lxml_binaries = collect_dynamic_libs('lxml')

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=lxml_binaries,
    datas=[
        ('json-styles/style.json', 'json-styles'),
        ('Qss/*', 'Qss'),
        ('Qss/icons/*', 'Qss/icons'),
        ('Qss/icons/icons/*', 'Qss/icons/icons'),
        ('Qss/icons/icons/feather/*', 'Qss/icons/icons/feather'),
        ('Qss/scss/*', 'Qss/scss'),
        ('fonts', 'fonts'),
        ('generated-files/*', 'generated-files'),
        ('config.json','.'),
        ('logo.png','.'),
        ('miniLogo.ico','.'),
        ('miniLogo.png','.'),
        ('Qss/icons/000000/*', 'Qss/icons/000000'),
        ('Qss/icons/000000/feather/*', 'Qss/icons/000000/feather'),
        ('Qss/icons/000000/font_awesome/brands/*', 'Qss/icons/000000/font_awesome/brands'),
        ('Qss/icons/000000/font_awesome/regular/*', 'Qss/icons/000000/font_awesome/regular'),
        ('Qss/icons/000000/font_awesome/solid/*', 'Qss/icons/000000/font_awesome/solid'),
        ('Qss/icons/000000/material_design/*', 'Qss/icons/000000/material_design'),
        ('Qss/icons/icons/*', 'Qss/icons/icons'),
        ('Qss/icons/icons/feather/*', 'Qss/icons/icons/feather'),
        ('Qss/icons/icons/font_awesome/brands/*', 'Qss/icons/icons/font_awesome/brands'),
        ('Qss/icons/icons/font_awesome/regular/*', 'Qss/icons/icons/font_awesome/regular'),
        ('Qss/icons/icons/font_awesome/solid/*', 'Qss/icons/icons/font_awesome/solid'),
        ('Qss/icons/icons/material_design/*', 'Qss/icons/icons/material_design'),
        ('Qss/scss/*', 'Qss/scss'),
        
        ],
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
)


coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main'
)