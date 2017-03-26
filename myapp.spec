rom kivy.deps import sdl2, glew
block_cipher = None

# added because of hidden modules
my_hidden_modules = [
         ( 'C:\\Users\\<username>\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\win32\\lib\\win32timezone.py', '.' )
         ]  

a = Analysis(['C:\\Users\\<username>\\Desktop\\MyApp\\myapp.py'],
             pathex=['C:\\Users\\<username>\\Desktop\\MyPackagedApp'],
             binaries=[],
             datas = my_hidden_modules,  # modified because of hidden modules
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='MyApp',
          debug=True,
          strip=False,
          upx=True,
          console=True , icon='C:\\Users\\<username>\\Desktop\\MyApp\\icon.ico')
coll = COLLECT(exe,Tree('C:\\Users\\<username>\\Desktop\\MyApp\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
			   *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name='MyApp')
