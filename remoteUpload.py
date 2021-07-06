import os
import glob

from base64 import b64encode, decode

import itertools
import numpy as np
import json

import argparse

from sshtunnel import SSHTunnelForwarder
import pymongo

MONGO_HOST = 'sonicthings.org' 
SERVER_USER   = 'prashanth' 
PRIVATE_KEY = '/Users/alex/Downloads/pvt' #

MONGO_USER='prashanth' #prashanth is only available user now
MONGO_PASS ='crab1Cannon!' 

MONGO_DB = "DSSynths"

# define ssh tunnel
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username=SERVER_USER,
    ssh_pkey=PRIVATE_KEY,
    remote_bind_address=('127.0.0.1', 27017)
)

# start ssh tunnel
server.start()

connection = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
mydb = connection[MONGO_DB]
mycol = mydb["synths"]


myConfig = {}

def get_arguments():
    parser = argparse.ArgumentParser(description="myParser")
    parser.add_argument("--configfile", required=True)
    parser.add_argument("--wavfiles", required=True)
    parser.add_argument("--zipfiles", required=True)    
    return parser.parse_args()

def main():

    # folderConsistency()

    dbobject = {}
    wav_file = []
    wav_file_names = []

    args = get_arguments()
    module_name = args.configfile # here, the result is the file name, e.g. config or config-special
    wavfiles = args.wavfiles # directory or file
    zipfile = args.zipfiles

    if os.path.isdir(wavfiles):

        for file in glob.glob(wavfiles +"/*.wav"):
            wav_file.append(open(file, "rb").read())
            wav_file_names.append(file)
        print(wav_file_names)
    else:
        wav_file.append(open(wavfiles, "rb").read())
        wav_file_names.append(wavfiles)

    with open(module_name) as json_file:
        MyConfig = json.load(json_file)
        print("Reading parameters for generating ", MyConfig['soundname'], " texture.. ")
    
    # Synth configuration
    dbobject["description"] = MyConfig["description"]
    dbobject["soundname"] = MyConfig["soundname"]
    dbobject["samplerate"] = MyConfig["samplerate"]
    dbobject["chunkSecs"] = MyConfig["chunkSecs"]
    dbobject["soundDuration"] = MyConfig["soundDuration"]
    dbobject["recordFormat"] = MyConfig["recordFormat"]
    variations = MyConfig["soundDuration"]/MyConfig["chunkSecs"]

    # Synth parameters

    userRange = []
    synthRange = []
    paramArr = MyConfig["params"]
    fixedParams = MyConfig["fixedParams"]

    for p in MyConfig["params"]:
        userRange.append(np.linspace(p["user_minval"], p["user_maxval"], p["user_nvals"], endpoint=True))
        synthRange.append(np.linspace(p["synth_minval"], p["synth_maxval"], p["user_nvals"], endpoint=True))

    userParam = list(itertools.product(*userRange))
    synthParam = list(itertools.product(*synthRange))

    paramsArr = []
    for p in paramArr:
        paramsArr.append(p["synth_pname"])

    for p in fixedParams:
        paramsArr.append(p["synth_pname"])


    dbobject["params"] = paramsArr
    dbobject["numFiles"] = len(userParam)*variations

    zip_file = open(zipfile, "rb").read()

    b64_zipfile = b64encode(zip_file)
    b64_wavfile = []
    dbobject["wavfile"] = []

    for index in range(len(wav_file)):
        dbobject["wavfile"].append({"name": wav_file_names[index], "raw_data": b64encode(wav_file[index])})

    #

    # dbobject["wavfile"] = b64_wavfile.decode("utf-8")
    dbobject["zipfile"] = b64_zipfile.decode("utf-8")
    # b64_zipfile.decode("utf-8")

    #print(dbobject["zipfile"])

    mycol.insert_one(dbobject)

if __name__ == '__main__':
    main()