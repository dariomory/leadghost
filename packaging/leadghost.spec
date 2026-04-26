# PyInstaller spec for a Windows one-file build (see .github/workflows/publish.yml).
# Run from repo root: pyinstaller packaging/leadghost.spec
# -*- mode: python ; coding: utf-8 -*-
# PyInstaller does not set __file__ in spec context; `SPEC` is the path to this file.
import os

from PyInstaller.building.api import EXE, PYZ
from PyInstaller.building.build_main import Analysis
from PyInstaller.utils.hooks import collect_all

_spec_dir = os.path.dirname(os.path.abspath(SPEC))
_root = os.path.normpath(os.path.join(_spec_dir, os.pardir))
_main = os.path.join(_root, "src", "leadghost", "__main__.py")
_src = os.path.join(_root, "src")

packages = (
    "selenium",
    "chromedriver_autoinstaller",
    "tldextract",
    "typer",
    "click",
    "rich",
    "pandas",
    "numpy",
    "PIL",
    "bs4",
    "dns",
    "certifi",
)

datas, binaries, hiddenimports = [], [], []
for name in packages:
    d, b, h = collect_all(name)
    datas += d
    binaries += b
    hiddenimports += h

a = Analysis(
    [str(_main)],
    pathex=[_src],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports
    + [
        "typer",
        "leadghost",
        "leadghost.bot",
        "leadghost.cli",
        "leadghost.selenium_bot",
    ],
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
    a.binaries,
    a.datas,
    [],
    name="leadghost",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
