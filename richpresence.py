from pypresence import Presence
import psutil
import time

client_id = "775637920333037579"  # Put your Client ID in here
RPC = Presence(client_id)

RPC.connect()

while True:
    cpu_per = round(psutil.cpu_percent(),1)
    print(psutil.cpu_freq())
    cpu_freq = round(psutil.cpu_freq().current)/1000
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)

    print(
        RPC.update(
            details="RAM: "+str(mem_per)+"%", 
            state="CPU: "+str(cpu_per)+"% @ " + str(cpu_freq) + "GHz",
            large_image="emcjforu4aamc8k",
            large_text="I simp for Gamer Gura.",
            small_image="shaark",
            small_text="Gura is hydrodynamic!",
            party_id="Fake Party ID!",
            join="Fake Join ID!",
            #start=start
        )
    )
    time.sleep(15)