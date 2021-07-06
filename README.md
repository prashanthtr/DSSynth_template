
# DSSynth_template for creating and uploading new synths

# Directory structure

DSSynth_template
 -- Synths
 -- remoteUpload.py
 -- Sample wave files
 -- Synth.zip 

# Instructions for running DSSynth_template

See the README file inside the synths for setting up template.


# Instructions for Remote Upload

## Setup DSSynth_template environment

  >> git clone https://github.com/prashanthtr/DSSynth_template.git

  >> cd DSSynth_template/

  >> conda create -n DSSynth_template python=3.8 ipykernel numba

  >> conda activate DSSynth_template

  >> pip install -r requirements.txt --src '.'

## Remote upload to sonicthings.org

>> python remoteUpload.py --configfile config_file.json --wavfiles dataset_sample_audio --zipfiles Synth.zip

# Sample template 

The DSsynth template includes a Pop texture as sample template file for creating new synthesizers.

