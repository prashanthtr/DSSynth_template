
# DSSynth_template for creating new synths

>> conda activate DSSynth_template

# Setup and run jupyter notebook

>> pip install jupyter

>> python3.8 -m ipykernel install --user --name DSSynth_template

>> jupyter notebook

>> Select *popTexture-notebook.ipynb* in the browser interface

## Generate files from commandline

>> python DSGenerator/generate.py --configfile config_file.json --outputpath NewDataset


## Setup to reinstall dssynth modules

>> pip install -r requirements.txt --src '.'

# Sample template 

The DSsynth template includes a Pop texture as sample template file for creating new synthesizers.

