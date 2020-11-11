from pypresence import Presence
import uptime
import psutil
import os
import cpuinfo
import time
import json

config = None

try:
    config = json.load(open("./config.json", 'r'))
    print("Successfully loaded config.json")
    print(config)
except:
    print("config.json does not exist.")
    

if not (config == None):
    client_id = config["client_id"]
    RPC = Presence(client_id)

    cpu_name = cpuinfo.get_cpu_info()["brand_raw"]
    start_time = time.time() - uptime.uptime()

    

    try:
        RPC.connect()
        print("Found Discord!")
    except:
        connected = False
        print("Searching for Discord.")

        while True:
            try:
                RPC.connect()
                connected = True
            except:
                connected = False

            if connected == True:
                print("Found Discord!")
                break

            time.sleep(1)



    while True:
        cpu_per = round(psutil.cpu_percent(),1)
        cpu_freq = round(psutil.cpu_freq().current/1000)
        mem = psutil.virtual_memory()
        mem_per = round(mem.percent,1)

        gameId = None

        topText = ""
        bottomText = ""

        cpuAddon = ""

        if config["includeUptime"] == False:
            start_time = None

        if config["includePartyInvite"] == True:
            gameId = "ayaya"

        if config["includeCPU_frequency"] == True:
            cpuAddon = cpuAddon + "@ " + str(cpu_freq) + "GHz "

        if config["includeCPU_model"] == True:
            cpuAddon = cpuAddon + "(" + cpu_name + ")"



        if config["order"][0] == "CPU":
            topText = "CPU: "+str(cpu_per)+"% " + cpuAddon
        elif config["order"][0] == "RAM":
            topText = "RAM: "+str(mem_per)+"% (" + str(round(mem.used / 1000000000, 2)) + "/" + str(round(mem.total / 1000000000, 2)) + " GB)"

        if config["order"][1] == "CPU":
            bottomText = "CPU: "+str(cpu_per)+"% " + cpuAddon
        elif config["order"][1] == "RAM":
            bottomText = "RAM: "+str(mem_per)+"% (" + str(round(mem.used / 1000000000, 2)) + "/" + str(round(mem.total / 1000000000, 2)) + " GB)"



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
                    join=gameId + gameId,
                    start=start_time
            )

            time.sleep(15)
        except:
            print("Lost connection to discord.")
            connected = False
            while True:

                try:
                    RPC.connect()
                    connected = True
                except:
                    connected = False#

                if connected == True:
                    print("Found Discord!")
                    break

                time.sleep(1)