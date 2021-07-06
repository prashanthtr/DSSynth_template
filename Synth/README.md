
# DSSynth_template for creating new synths

# Setting up DSSynth_template

## User instructions

  >> git clone https://github.com/prashanthtr/DSSynth_template.git

  >> cd DSSynth_template/

  >> conda create -n DSSynth_template python=3.8 ipykernel numba

  >> conda activate DSSynth_template

  >> pip install -r requirements.txt --src '.'

# Setup and run jupyter notebook

>> pip install jupyter

>> python3.8 -m ipykernel install --user --name DSSynth_template

>> jupyter notebook

>> Select *popTexture-notebook.ipynb* in the browser interface

## Generate files from commandline

>> python DSGenerator/generate.py --configfile config_file.json --outputpath NewDataset

# Sample template 

The DSsynth template includes a Pop texture as sample template file for creating new synthesizers.

