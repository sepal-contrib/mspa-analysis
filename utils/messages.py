##########################################
##             file selection           ##
##########################################
FILE_INPUT = "Select the file to be processed"
FILE_SELECT = "Validate input"
NO_FILE = "No file has been selected" 
WRONG_FILE = "The file {} does not exist"
WRONG_FILE_TYPE = "The file {} is not a geotif format"
TOO_BIG = "The file is too big, use a bigger AWS instance and relaunch the app"
FILE_TXT = """
The file input need to be a `.tif` or a `.tiff` file. It will be the only file type available in the file selector.  
If your raster has multiple bands, only the **first one** will be used in this module to describe the forest and the non-forest areas.
"""

###########################################
###         bands selection             ###
###########################################
BANDS_INTRO = "Select the classes that will be tagged as foreground (2) and background (1) in the binary map. The remaining classes will be tagged as no-data (0). Be carreful not to select a class twice."
BANDS_BTN = "Validate your values selection"
NO_BANDS = "You didn't select values for forest and/or non-forest description"
BANDS_VALID = "Your values selection have been validated"
BANDS_OVERRIDE = "You selected at least one value twice. Please verify your inputs"
BIN_MAP_READY = "The bin map was already ready you can launch the MSPA process"
END_BIN_MAP = "The bin map have been successfully created"

##########################################
##             mspa process             ##
##########################################
MSPA_NO_RESULTS = 'No results to display yet'
MSPA_MESSAGE = "Launch MSPA analysis on your data"
MSPA_BTN = 'Run MSPA analysis'
RUN_MSPA = 'Run MSPA with "{}" inputs'
MSPA_MAP_READY = "the MSPA map was already ready"
NO_MAP = "No bin map can be used in this configuration. Please rerun to the value selection process"
NO_INPUT = "Please check that all the MSPA process input have be initialized"
ERROR_MSPA = "An error occured during the execution of the MSPA process. Try running a bigger AWS instance and relaunch the app"
