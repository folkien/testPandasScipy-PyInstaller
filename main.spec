# -*- mode: python -*-
block_cipher = None

def get_pandas_path():
    import pandas
    pandas_path = pandas.__path__[0]
    return pandas_path

def get_scipy_path():
    import scipy
    pandas_path = scipy.__path__[0]
    return pandas_path

a = Analysis(['main.py'],
         pathex=[],
         binaries=None,
         datas=None,
         hiddenimports=[],
         hookspath=None,
         runtime_hooks=None,
         excludes=None,
         win_no_prefer_redirects=None,
         win_private_assemblies=None,
         cipher=block_cipher)

# Fix pandas imports
dict_tree = Tree(get_pandas_path(), prefix='pandas', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'pandas' not in x[0], a.binaries)

# Fix scipy imports
dict_tree = Tree(get_scipy_path(), prefix='scipy', excludes=["*.pyc"])
a.datas += dict_tree
a.binaries = filter(lambda x: 'scipy' not in x[0], a.binaries)

pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      exclude_binaries=True,
      name='Main',
      debug=False,
      strip=None,
      upx=True,
      console=True )
scoll = COLLECT(exe,
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=None,
           upx=True,
           name='Main')

