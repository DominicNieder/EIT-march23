import plotting as p

from fitting import fit_gaussian
from utils import keep_log, read_entry, read_folder, open_log, post_log

from handling_data import load_spectrum, load_all_spectra, load_coincidence

import func 
import os
import numpy as np
#--------------------------------------------------
#           Here the Analysis shall be performed
#--------------------------------------------------


### select which part of the analysis shall be performed

run =           False


# all directories       
dir_data = "../data"
dir_figures = "../figures"
dir_pictures = "../pictures"


# analysis section
def callibration():
    data_loc = "/calibration"


# execution:
if run:
    callibration()