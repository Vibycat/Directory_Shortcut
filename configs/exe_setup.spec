# PyInstaller spec file for creating an executable
block_cipher = None

a = Analysis(
    ['Setup_New_Project.py'],  # Update with your main script name
    pathex=[],
    binaries=[],
    datas=[('G:\\git_portfolio\\Setup_New_Git_Pro\\templates\\*', 'templates')],  # Include templates folder
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='my_program',  # Base executable name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True  # Set to False if GUI app
)
