import os
import glob

from base64 import b64encode, decode

import itertools
import numpy as np
import json
import argparse
from sshtunnel import SSHTunnelForwarder
import pymongo


# Collection variables
mycol = {}
myConfig = {}

def main ():

    args = get_arguments()
    module_name = args.configfile # here, the result is the file name, e.g. config or config-special

    with open(module_name) as json_file:
        templateConfig = json.load(json_file)
        print("Reading parameters for generating ", templateConfig['soundname'], " texture.. ")

    MONGO_HOST = templateConfig["MONGO_HOST"]
    SERVER_USER   = templateConfig["SERVER_USER"]
    SERVER_PWD = templateConfig["SERVER_PWD"]
    PRIVATE_KEY = templateConfig["PRIVATE_KEY"]
    MONGO_USER= templateConfig["MONGO_USER"] #prashanth is only available user now
    MONGO_DB = templateConfig["MONGO_DB"]
    MONGO_COLLECTIONS = templateConfig["MONGO_COLLECTIONS"]

    try:

        if SERVER_PWD != "" : 
            with SSHTunnelForwarder(
                MONGO_HOST,
                ssh_username=SERVER_USER,
                ssh_pkey=PRIVATE_KEY,
                ssh_private_key_password=SERVER_PWD, 
                remote_bind_address=('127.0.0.1', 27017)
            ) as server:
                print("connected")

        else:
            with SSHTunnelForwarder(
                        MONGO_HOST,
                        ssh_username=SERVER_USER,
                        ssh_pkey=PRIVATE_KEY,
                        remote_bind_address=('127.0.0.1', 27017)
                ) as server:
                    print("connected")

    except Exception as e:
            print("Not connected because: " + e)

        # start ssh tunnel
    else:

        server.start()
        print("connected to server")
        connection = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
        mydb = connection[MONGO_DB]
        mycol = mydb[MONGO_COLLECTIONS]
        update(templateConfig, mycol)

def get_arguments():
    parser = argparse.ArgumentParser(description="myParser")
    parser.add_argument("--configfile", required=True)
    parser.add_argument("--wavfiles", required=True)
    parser.add_argument("--zipfiles", required=True)    
    return parser.parse_args()

def update (MyConfig, mycol):

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
        #print(wav_file_names)
    else:
        wav_file.append(open(wavfiles, "rb").read())
        wav_file_names.append(wavfiles)


    # Synth configuration
    dbobject["description"] = MyConfig["description"]
    dbobject["soundname"] = MyConfig["soundname"]

    #dbobject["samplerate"] = MyConfig["samplerate"]
    
    try:
        with open(os.path.join(MyConfig["soundname"], "config_file.json")) as json_file:
             synthConfig = json.load(json_file)
    except:
        print("Create config file in synth folder")

    else:

        dbobject["chunkSecs"] = synthConfig["chunkSecs"]
        dbobject["soundDuration"] = synthConfig["soundDuration"]
        dbobject["recordFormat"] = synthConfig["recordFormat"]
        variations = synthConfig["soundDuration"]/synthConfig["chunkSecs"]

        # Synth parameters

        userRange = []
        synthRange = []
        paramArr = synthConfig["params"]
        fixedParams = synthConfig["fixedParams"]

        for p in synthConfig["params"]:
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

        print(dbobject)

        zip_file = open(zipfile, "rb").read()

        b64_zipfile = b64encode(zip_file)
        b64_wavfile = []
        dbobject["wavfile"] = []


        if len(wav_file) == 0:            
            print(" Please provide atleast 1 sample wav file")

        else:
            for index in range(len(wav_file)):
                dbobject["wavfile"].append({"name": wav_file_names[index], "raw_data": b64encode(wav_file[index])})

            # dbobject["wavfile"] = b64_wavfile.decode("utf-8")
            dbobject["zipfile"] = b64_zipfile.decode("utf-8")
            # b64_zipfile.decode("utf-8")

            #print(dbobject["zipfile"])
            mycol.insert_one(dbobject)

if __name__ == '__main__':
    main()