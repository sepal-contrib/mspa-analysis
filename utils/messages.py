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