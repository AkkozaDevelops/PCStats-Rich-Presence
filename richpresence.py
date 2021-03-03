
print("Created by AkkozaDevelops\n\nGitHub Repo: https://github.com/AkkozaDevelops/PCStats-Rich-Presence\n\nIssues? you can either\nAdd me on Discord [Akkoza#3400]\nOR\nCreate a issue request on the Github Repo")
# You don't have to keep this, but I would rather you do <3

import time
import re

try:
    from pypresence import Presence
    import uptime
    import psutil
    import os
    import cpuinfo
    import json
except Exception as e:
    print("\nPlease make sure you installed all the dependancies!\n\nYou can easily install them all by running the \"python dependancies.bat\" file in the GitHub Repo\n[https://github.com/AkkozaDevelops/PCStats-Rich-Presence]")
    print("\n\nError:\n" + str(e))

    while True:
        time.sleep(1)

me = os.path.dirname(os.path.abspath(__file__))     

config = None

try:
    config = json.load(open(me + "/config.json", 'r'))
    print("Successfully loaded config.json")
    print("\n\nConfig file reads:\n" + str(config))
except Exception as e:
    print("config.json does not exist.")
    print("Error\n" + str(e))
    

if not (config == None):
    client_id = config["client_id"]
    RPC = Presence(client_id)

    cpu_name = cpuinfo.get_cpu_info()["brand_raw"]
    start_time = time.time() - uptime.uptime()


    if config["order"][0] == "GPU" or config["order"][1] == "GPU":
        try:
            import GPUtil

            if len(GPUtil.getGPUs()) == 0:
                print("\n\nYou do not have any NVIDIA GPUs installed in your system!")

                while True:
                    time.sleep(1)
        except:
            print("\n\nPlease install the GPUtil package!\nRestart this program when you have installed it.")
            
            while True:
                time.sleep(1)
    

    try:
        RPC.connect()
        print("\nFound Discord!")
    except Exception as e:
        if str(e) == "Pipe Not Found - Is Discord Running?":
            connected = False
            print("\nSearching for Discord.")

            while True:
                try:
                    RPC.connect()
                    connected = True
                except:
                    connected = False

                if connected == True:
                    print("\nFound Discord!")
                    break

                time.sleep(1)
        else:
            print("There was an error\n\n" + str(e))



    while True:
        cpu_per = round(psutil.cpu_percent(),1)
        cpu_freq = round(psutil.cpu_freq().current/1000)
        mem = psutil.virtual_memory()
        mem_per = round(mem.percent,1)

        gameId = None
        joinId = None

        buttonsContainer = None

        topText = ""
        bottomText = ""

        cpuAddon = ""

        if config["includeUptime"] == False:
            start_time = None

        if config["includePartyInvite"] == True:
            gameId = "ayaya"
            joinId = "boobs"

        if config["includeCPU_frequency"] == True:
            cpuAddon = cpuAddon + "@ " + str(cpu_freq) + "GHz "

        if config["includeCPU_model"] == True:
            cpuAddon = cpuAddon + "(" + cpu_name + ")"

        if config["buttonsEnabled"] == True:
            newTable = []
            

            for table in config["buttons"]:
                if table["label"] and table["label"] != "":
                    if table["url"] and table["url"] != "":
                        newTable.insert(len(newTable)+1, table)

            buttonsContainer = newTable



        if config["order"][0] == "CPU":
            topText = "CPU: "+str(cpu_per)+"% " + cpuAddon
        elif config["order"][0] == "RAM":
            topText = "RAM: "+str(mem_per)+"% (" + str(round(mem.used / 1000000000, 2)) + "/" + str(round(mem.total / 1000000000, 2)) + " GB)"
        elif config["order"][0] == "GPU":
            topText = "GPU: " + str(GPUtil.getGPUs()[0].load * 100) + "% (" + str(round(GPUtil.getGPUs()[0].memoryUsed / 1000, 1)) + "/" + str(round(GPUtil.getGPUs()[0].memoryTotal / 1000, 1)) + "GB)"

        if config["order"][1] == "CPU":
            bottomText = "CPU: "+str(cpu_per)+"% " + cpuAddon
        elif config["order"][1] == "RAM":
            bottomText = "RAM: "+str(mem_per)+"% (" + str(round(mem.used / 1000000000, 2)) + "/" + str(round(mem.total / 1000000000, 2)) + " GB)"
        elif config["order"][1] == "GPU":
            bottomText = "GPU: " + str(GPUtil.getGPUs()[0].load * 100) + "% (" + str(round(GPUtil.getGPUs()[0].memoryUsed / 1000, 1)) + "/" + str(round(GPUtil.getGPUs()[0].memoryTotal / 1000, 1)) + "GB)"



        if bottomText == "":
            bottomText = None
        
        if topText == "":
            topText = None
            
        try:
            RPC.update(
                    details=topText,
                    state=bottomText,
                    large_image=config["images"]["large_image"],
                    large_text=config["hover_text"]["large_image_text"],
                    small_image=config["images"]["small_image"],
                    small_text=config["hover_text"]["small_image_text"],
                    party_id=gameId,
                    join=joinId,
                    buttons=buttonsContainer,
                    start=start_time
                    )

            time.sleep(15)
        except Exception as e:
            if str(e) == "Pipe Not Found - Is Discord Running?" :
                print("\nLost connection to discord.")
                connected = False
                while True:

                    try:
                        RPC.connect()
                        connected = True
                    except:
                        connected = False#

                    if connected == True:
                        print("\nFound Discord!")
                        break

                time.sleep(1)
            elif str(e) == "Client ID is Invalid":
                print("\nMake sure your Client ID is valid!\n")

                while True:
                    time.sleep(1)
            else:
                print("There was an error\n\n" + str(e))

                while True:
                    time.sleep(1)
            
