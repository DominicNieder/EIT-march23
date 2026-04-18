# EIT Experiment

## Preliminaries

### Github settings
- fist add a file named ".gitignore" this will automatically be recognised by Git, so that it ignores all files (pdf for reading, *.log, etc...) that are not required to be shared.
Here is the content of my `.gitignore` file:

```gitignore
# my literature to read (comments in .gitignore)
reading/
analysis-code/__pycache__

# any other pdf, also from .tex
*.pdf

# latex specific
*.out
*.fls
*.log
*.xml
*.sta
*.gz
*.aux
*.bbl
*.fdb_latexmk
*.bcf
*.blg
*.toc

# do not change
.gitignore

# my python environment
analysis-code/.compton_environment/
```


### Report and Latex

Depending on from which directory the "main.tex" will be compiled from, the **figures/picutres will be accessed by a different path**. 

In report/main.tex there is a line that will access all figures from figure/ and, or pictures/ (line 22)
> \graphicspath{{../figures/}{../pictures/}}

run from commandline:
> cd report && pdflatex main.tex



### Python coding

The necessary packages are in "analysis-code/requirements.txt". 

##### Workflow: using pip (venv) 
Create python environment in analysis-code, i.e. with "venv" using BASH:
> python3 -m venv analysis-code/.compton_environment

To activate it type
> source analysis-code/.compton_environment/bin/activate

Use
> which pip

**to make sure you are using the correct environment!**

To **install all packages** which are used:
> which pip
> pip install -r requirements.txt

If you **add a different package** (make sure your **correct environment is active!**):
> which pip
> pip install PACKAGE_NAME
> pip freeze > requirements.txt

Thus the "requirements.txt is up-to-date, including all packages that might be used.


##### Wrokflow: organisation
The analysis should be carried out in main.py!
Functions should be defined in the appropriate file! Add further files if needed. 
Keep track of packages being used.

Access functions in main.py i.e. by the following:
```python
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
```



### Data, Figures, Pictures, Results

- The meausrements -> data/
- plots (i.e. from analysis) go to figures/
- photos -> pictures/
- results from analysis -> results/

Every directory contains an "orientation.txt" file. This should help to keep log, enabling concise naming of files, with descriptions.



## Questions

We shall come across many questions. For the preparation, in our experimental procedure should be based on questions we want to reason and to reach a goal.


### Preparation questions

Introduction text:
- Setup and principle of operation of Scintillation Spectrometry
- Functional principle of the devices used to take the measurements
- Relevance of linear and logic pulses
- Difference between organic and anorganic scintillators
- Interaction of $\gamma$ rays and electrons with matter
- Definition and measurement of differential and total cross sections

### Experimental procedure


### Questions for the Supervisor


## Required measurements


### Preparation
- Resolution of detector: $R=\Delta E/E$, with $\Delta E=FWHM$ of photo peak (for Cs$^{137}$ possible to obtain below 8%)