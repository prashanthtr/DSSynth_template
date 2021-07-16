
# DSSynth_template for creating and uploading new synths

# Directory structure

DSSynth_template
 -- SynthName_folder
 -- Sample_wave_files_folder
 -- SynthName.zip 
 -- remoteUpload.py
 -- requirements.txt

# Instructions for running DSSynth_template

## Cloning and installing

  >> git clone https://github.com/prashanthtr/DSSynth_template.git

  >> cd DSSynth_template/

  >> conda create -n DSSynth_template python=3.8

  >> conda activate DSSynth_template

  >> pip install -r requirements.txt --src '.'

# Instructions for creating synths and generating datasets
	Refer to Readme inside SynthName_folder

# Instructions for Remote Upload to sonicthings.org

## Setting up template configuration file

      "description": " A description of the synth" <e.g., drip texture is a fast frequency sweep over 50hz>
	  "soundname": "DripPatternSynth",
      "MONGO_HOST": "sonicthings.org", 
      "SERVER_USER": "", <request user name otherwise> 
      "PRIVATE_KEY": "",
      "SERVER_PWD": "",  <If required, otherwise leave this as blank>
      "MONGO_USER": "",  <request username>
      "MONGO_DB": "DSSynths",
      "MONGO_COLLECTIONS": "synths"

## Clean synth directory with ./cleanDir.sh

## Create zip file for synth as @ SynthName.zip

## Create sample wav files for synth @ dataset_sample_audio 


# Upload to sonicthings.org via commandline

>> python remoteUpload.py --configfile config_file.json --wavfiles dataset_sample_audio --zipfiles Synth.zip

# Sample template 

The DSsynth template includes a Drip texture as sample template file for creating new synthesizers.

