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

##########################################################
#########                     legend                ######
##########################################################
mspa_colors = {
    'background': [220, 220, 220, 255],
    'branch': [255, 140, 0, 255],
    'perforation': [0, 0, 255, 255],
    'islet': [160, 60, 0, 255], 
    'core': [0, 220, 0, 255], 
    'bridge': [255, 0, 0, 255], 
    'loop': [255, 255, 0, 255],
    'edge': [0, 0, 0, 255],
    'no-data': [255, 255, 255, 255],
}

