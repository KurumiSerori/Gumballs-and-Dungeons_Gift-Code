from distutils.core import setup
import py2exe
import sys

#this allows to run it with a simple double click.
sys.argv.append('py2exe')

setup( windows = ['GiftCode.py'],
       zipfile = None,
       options = {'py2exe':{
           "bundle_files": 1,
           "dll_excludes":["MSVCP90.dll", "w9xpopen.exe"]
           }
        }
)
