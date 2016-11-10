'''
sp: small project
'''
import sys
import sqlite3

from importlib import import_module
import module

print('import module ...')
modules = []
moduleDict = {}
for name in module.__all__:
    pkg='module'
    print('import', name)
    mod = import_module('%s.%s'%(pkg, name), pkg)
    modules.append(mod)
    moduleDict[name] = mod

# global value
conn = None

def get_karg():
    for arg in sys.argv:
        
    


def get_dbfile():
    ''' 
    default dbfile in located in home
    
    '''

def mainfunc():
    global conn #global value
    try:
        dbfile = sys.argv[1]
        conn = sqlite3.connect(dbfile)
    except IndexError:
        print('**Error: database file not specified')
        print('    sp dbfile [...]')
        print('    create new db: sp init dbfile')
    
    
    
    
if __name__ == '__main__':
    mainfunc()
