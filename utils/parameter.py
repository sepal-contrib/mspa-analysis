#hard coded parameters 

import os
from pathlib import Path

#####################
##     folders     ##
#####################

def create_folder(pathname):
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    return pathname

def getResultDir():
    pathname = os.path.join(os.path.expanduser('~'), 'mspa_results') + '/'
    return create_folder(pathname)

def getRootDir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pathname = Path(dir_path).parent
    print(pathname)
    return pathname

def getMspaDir():
    pathname = os.path.join(getRootDir(), 'mspa') + '/'
    return create_folder(pathname)

def getTmpMspaDir():
    pathname = os.path.join(getResultDir(), 'mspa') + '/'
    return create_folder(pathname)


