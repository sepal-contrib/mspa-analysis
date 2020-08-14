##########################################
##             file selection           ##
##########################################
FILE_INPUT = "Select the file to be processed"
FILE_SELECT = "Validate input"
NO_FILE = "no file has been selected" 
WRONG_FILE = "The file {} does not exist"
WRONG_FILE_TYPE = "The file {} is not a geotif format"
TOO_BIG = "The file is to big, use a bigger AWS instance and relaunch the app"


###########################################
###         bands selection             ###
###########################################
BANDS_INTRO = "select the band that will be tagged as forest (2) and non-forest (1). The remaining bands will be tagged as no-data (0). Be carreful not to select a band twice."
BANDS_BTN = "Validate your band selection"
NO_BANDS = "You didn't select bands for forest and/or non-forest description"
BANDS_VALID = "Your band selection have been validated"
BANDS_OVERRIDE = "You selected at least a band twice. Please verify your inputs"
BIN_MAP_READY = "The bin map was already ready you can launch the mspa process"
END_BIN_MAP = "The bin map have been successfully created"

##########################################
##             mspa process             ##
##########################################
MSPA_NO_RESULTS = 'No results to display yet'
MSPA_MESSAGE = "Launch MSPA analysis on your data"
MSPA_BTN = 'Run mspa analysis'
RUN_MSPA = 'Run mspa with "{}" inputs'
MSPA_MAP_READY = "the MSPA map was already ready"
NO_MAP = "no bin map can be used in this configuration. Please rerun the band selection process"
NO_INPUT = "please check that all the mspa process input have be initialized"
ERROR_MSPA = "An error occured during the execution of the MSPA process. Try running a bigger AWS instance and relaunch the app"
