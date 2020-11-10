## Discord Rich Presence

Discord has a cool application feature that allows you to add a rich presence to a user.
![picture of rich presence on my user.](https://i.imgur.com/cxfcTBX.png)

## How to setup

To start off, you need Python >=3.5 *[make sure to install with PATH]*, and Visual Studio 2019 with the C++ Desktop Development Package *[for psutil package]*

You also need to install these packages using these commands in the command prompt.

> pip install --user pypresence
> pip install --user psutil

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

Once you upload all your assets, you're ready to start editing the script.
I recommend using **Visual Studio Code** to edit this, but **Notepad** will work just as well!

You'll want to change the **client_id** variable to your own client id, which you can get in the **General Information** tab!

![image showing the client id, and the "copy" button.](https://i.imgur.com/skaaw60.png)

Once you grab your client id, go ahead and replace it!

So onto changing the images and their text.

You need to get those snazzy asset names from what you just uploaded for the images, and replace them for the **large_image** and or **small_image** values.
![showing large_image and small_image values](https://i.imgur.com/yhixBlG.png)


If you don't wish to have hover text or a image in a certain section, you can **completely remove** the section from the **RPC update**

![deleting large_image and large_text field](https://i.imgur.com/pBDDoN5.gif)

And if you don't wish to have the "game" invite feature, you can remove the **party_id** line and the **join** line
![gif of me deleting the lines.](https://i.imgur.com/TKaSXl9.gif)

## Once you've done all of this, you are ready to run the script!

If you have **ANY** issues, please open an issue through GitHub 😊
