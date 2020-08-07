import os
import psutil
from sepal_ui.scripts import utils as su
from utils import messages as ms
import rasterio as rio
import numpy as np

def validate_file(file, output):
    
    #check that the file exist
    if not os.path.isfile(file):
        su.displayIO(output, ms.WRONG_FILE.format(file), 'error')
        return None
    
    #check that the file is a tif 
    if not file.lower().endswith(('.tif', '.tiff')):
        su.displayIO(output, ms.WRONG_FILE_TYPE.format(file), 'error')
        return None
    
    #check the file size 
    if  os.path.getsize(file) > psutil.virtual_memory()[1]/2: #available memory
        su.displayIO(output, ms.TOO_BIG, 'error')
        return None
    
    #readt the file 
    with rio.open(file) as src:
        info = src.read(1, masked=True)

    #extract the frequency of each value 
    array = np.array(info.ravel())
    values = np.unique(array)
    
    return values