import os
import glob

def get_tif():
    """retreive all the tif file path from sepal directory"""
    
    #TODO would be better with a select
    
    root_dir = os.path.expanduser('~')
    raw_list = glob.glob(root_dir + "/**/*.tif", recursive=True)

    return raw_list