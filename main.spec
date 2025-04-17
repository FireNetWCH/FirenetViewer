# -*- mode: python ; coding: utf-8 -*-

import sys ;
from PyInstaller.utils.hooks import collect_data_files
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

pyvis_datas = collect_data_files('pyvis')
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[ ('json-styles/style.json', 'json-styles'),
        ('Qss/scss/*', 'Qss/scss'),
        ('fonts', 'fonts'),
        ('generated-files/*', 'generated-files'),
        ('config.json','.'),
        ('DejaVuSansCondensed.ttf','.'),
        ('logo.png','.'),
        ('miniLogo.png','.'),
        ('tagColor.json','.'),
        ('Qss/icons/FFFFFF/feather/copy.png','Qss/icons/FFFFFF/feather/'),
        ('Qss/icons/FFFFFF/feather/minus.png','Qss/icons/FFFFFF/feather/'),
        ('Qss/icons/FFFFFF/feather/x.png','Qss/icons/FFFFFF/feather/'),
        ('Qss/icons/FFFFFF/feather/home.png','Qss/icons/FFFFFF/feather/'),
        ('Qss/icons/FFFFFF/feather/activity.png','Qss/icons/FFFFFF/feather/'),
        ('Qss/icons/FFFFFF/feather/mail.png','Qss/icons/FFFFFF/feather/'),
        ('Qss/icons/FFFFFF/font_awesome/solid/chart-pie.png','Qss/icons/FFFFFF/font_awesome/solid/'),
        ('Qss/icons/FFFFFF/material_design/format_align_justify.png','Qss/icons/FFFFFF/material_design/'),
        ('Qss/icons/icons/font_awesome/regular/file-pdf.png','Qss/icons/icons/font_awesome/regular/'),
        ('Qss/icons/icons/font_awesome/solid/circle-xmark.png','Qss/icons/icons/font_awesome/solid/'),
        ('Qss/icons/icons/font_awesome/regular/file-code.png','Qss/icons/icons/font_awesome/regular/'),
        ('Qss/icons/icons/font_awesome/regular/calendar.png','Qss/icons/icons/font_awesome/regular/'),
        ('Qss/icons/black/feather/download.png','Qss/icons/black/feather/'),
        ('Qss/icons/black/font_awesome/solid/rss.png','Qss/icons/black/font_awesome/solid/'),
        ('Qss/icons/black/feather/linkedin.png','Qss/icons/black/feather/'),
        ('Qss/icons/black/feather/facebook.png','Qss/icons/black/feather/'),
        ('Qss/scss/*', 'Qss/scss'),
        *pyvis_datas],
    hiddenimports=['PySide6','openpyxl','openpyxl.cell._writer','_ctypes'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'PySide2', 'PyQt6'],
    noarchive=False,
    optimize=0,
)

splash = Splash('logo.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=(60, 60),
                text_size=12,
                text_color='black')

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    splash,
    splash.binaries, 
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon = 'C:\\Users\\firenet\\FirenetViewer_email_view\\FirenetViewer\\miniLogo.png'
)

