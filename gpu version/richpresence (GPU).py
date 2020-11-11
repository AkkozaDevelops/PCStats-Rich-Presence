from pypresence import Presence
import psutil
import GPUtil
import time

client_id = "CLIENT ID HERE"

if len(GPUtil.getGPUs()) == 0:
    print("Your system does not have any NVIDIA GPUs installed!")
else:
    RPC = Presence(client_id)

    RPC.connect()

    while True:
        cpu_per = round(psutil.cpu_percent(),1)
        cpu_freq = round(psutil.cpu_freq().current/1000, 2)
        mem = psutil.virtual_memory()
        mem_per = round(mem.percent,1)
        primary_gpu = GPUtil.getGPUs()[0]

        try:
            RPC.update(
                details="CPU: "+str(cpu_per)+"% @ " + str(cpu_freq) + "GHz",
                state="GPU: " + str(primary_gpu.load * 100) + "% (" + str(round(primary_gpu.memoryUsed / 1000, 1)) + "/" + str(round(primary_gpu.memoryTotal / 1000, 1)) + "GB)",
                large_image="CHANGE ME TO BIG IMAGE KEY",
                large_text="CHANGE ME TO WHAT YOU WANT HOVER TEXT TO BE",
                small_image="CHANGE ME TO SMALL IMAGE KEY",
                small_text="CHANGE ME TO WHAT YOU WANT HOVER TEXT TO BE",
                party_id="Fake Party ID!",
                join="Fake Join ID!"
            )
        except:
            print("There was an error; trying to reattach hook [Discord closed?]")
            RPC.connect()
        
        time.sleep(15)