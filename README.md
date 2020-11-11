
## Discord Rich Presence

  

Discord has a cool application feature that allows you to add a rich presence to a user.

  

![picture of rich presence on my user.](https://i.imgur.com/cxfcTBX.png)

  

## Start on Startup

  

You can easily have this run when your computer starts by putting it in your Startup Folder

  

You can get there by doing **WIN + R** or typing **run** in the Windows Search bar.

  

![picture of run](https://i.imgur.com/WYecEkf.png)

  

You then want to type the following into **Run** and press **OK**

  

> shell:startup

  

This will then open a folder, which you can drag the Python Script into.

  
  

## Difference between Console Version and No Console Version

  

Python has a different extension *[.pyw]* that is differnet from *[.py]* which just disables the console from ever appearing.

  

## How to setup

  

To start off, you need Python >=3.5 *[make sure to install with PATH]*, and Visual Studio Community 2019 with the **Desktop development with C++**  *[for psutil package]*

  

![showing selected package](https://cdn.discordapp.com/attachments/738968109288914976/775828681674719232/unknown.png)

  

You also need to install these packages using these commands in the command prompt **OR** you can run the **bat** file included in the GitHub repository.

  

> pip install --user pypresence

  

> pip install --user psutil

  

> pip install --user uptime

  

Once you install those 2 packages, you should be almost ready.

  

Next; you need to create a Discord Application through Discord's Developer Portal.

***[https://discord.com/developers/applications]***

  

![picture pointing towards the "New Application" button.](https://i.imgur.com/X7pE5BB.png)

  

**Make sure to name the Application after what you want the "game" to be named**

  

![image showing the "Create an Application" screen.](https://i.imgur.com/4OXlJVw.png)

  

Once you make your application, head on over to **"Rich Presence"**

  

![showing the location of the rich presence tab.](https://i.imgur.com/F9pxRlb.png)

  

This is where you'll want to upload all your image assets, and your "game" invite cover image.

  

![showing asset example.](https://i.imgur.com/g1BVyLI.png)

  

You'll need those asset names in a second for when we start editing the script.

*[Used for the image icons on the Rich Presence]*

  

Once you upload all your assets, you're ready to start editing the config file.

I recommend using **Visual Studio Code** to edit this, but **Notepad** will work just as well!

You'll want to open the **config.json** file that comes included in the GitHub Repository.  

When you open it, you'll want to change the **client_id** to your own client id, which you can get in the **General Information** tab!

  

![image showing the client id, and the "copy" button.](https://i.imgur.com/skaaw60.png)

Once you copy your client id, you can paste it into the  **client_id** section.
![gif of me replacing the client id](https://i.imgur.com/nTflHYL.gif)  

Once you set your **client id** you're finished, **BUT** if you want to include your snazzy assets you added and customize even further, you'll want to edit more.

To set your **large_image** and **small_image** you must change **null** into a **string** and put the **asset name** into it.

![gif of me adding a large and small image](https://i.imgur.com/Tnicg8q.gif)

*NOTE: YOU CAN LEAVE IT ANYTHING HERE AS NULL TO NOT INCLUDE IT*

To set the **hover text** of your large and small image, you do basically the same thing; You change **null** into a **string** and put whatever you want to show when you hover into it.

![gif of me setting the hover text.](https://i.imgur.com/Xhpwa82.gif)


So now onto changing the **CPU**, **RAM**, and **GPU** display!
*Due to Discord Rich Embed limits, you can only have 2 displayed.*
*GPU is still a WIP, and only works on NVIDIA GPUs atm.*

You can easily change the order of either **CPU**, **RAM**, or **GPU** by changing the order of them.
The default is **CPU**, and **RAM**; but you can easily change this by changing the **strings** in the **"order"** category between **"CPU"**, **"RAM"**, and **"GPU"**

![gif of me changing the order of CPU, RAM, and changing to GPU](https://i.imgur.com/fD2j62Z.gif)

*GPU requires another package, and will warn you to download it if you run it without the package.*

**If you choose GPU**, you will want to run this command in command prompt.

> pip install --user GPUtil

## Once you've done all of this, you are ready to run the script!

 

If you have **ANY** issues, please open an issue through GitHub 😊