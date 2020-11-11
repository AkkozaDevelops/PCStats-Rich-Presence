from pypresence import Presence
import psutil
import time

client_id = "CLIENT ID HERE"
RPC = Presence(client_id)

try:
    RPC.connect()
except:
    connected = False

    while True:
        try:
            RPC.connect()
            connected = True
        except:
            connected = False

        if connected == True:
            break

        time.sleep(1)


while True:
    cpu_per = round(psutil.cpu_percent(),1)
    cpu_freq = round(psutil.cpu_freq().current/1000, 2)
    mem = psutil.virtual_memory()
    mem_per = round(mem.percent,1)

    try:
        RPC.update(
            details="RAM: "+str(mem_per)+"% (" + str(round(mem.used / 1000000000, 2)) + "/" + str(round(mem.total / 1000000000, 2)) + " GB)", 
            state="CPU: "+str(cpu_per)+"% @ " + str(cpu_freq) + "GHz",
            large_image="CHANGE ME TO BIG IMAGE KEY",
            large_text="CHANGE ME TO WHAT YOU WANT HOVER TEXT TO BE",
            small_image="CHANGE ME TO SMALL IMAGE KEY",
            small_text="CHANGE ME TO WHAT YOU WANT HOVER TEXT TO BE",
            party_id="Fake Party ID!",
            join="Fake Join ID!"
        )
    except:
        connected = False

        while True:

            try:
                RPC.connect()
                connected = True
            except:
                connected = False

            if connected == True:
                break

            time.sleep(1)
    
    time.sleep(15)