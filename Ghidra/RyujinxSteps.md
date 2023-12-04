# How to port .pchtxt (ExeFS) Switch Mods from a previous udpate to a newer update. Mainly focus on emulators (Yuzu/Ryujinx)

### Steps to do in Ryujinx

I assume you already know how to setup Ryujinx: Setup prod.keys, firmware and set up your game folder directory so **I won’t explain it**. Otherwise use [this guide](https://github.com/Abd-007/Switch-Emulators-Guide/blob/main/Ryujinx.md) or this [video guide](https://youtu.be/a3lqX176K0w?t=110) so ... let's continue:

1. Right click on the game you want -> Manage Title Updates -> Add and search for the update. 

**Make sure you only select the update you want to extract the ExeFS files from**.

Remember that you will need 2 versions (the old one and the new one) and if you want to learn how everything works better in a better way, a third one (previous to these 2. **This suggestion is just for starters**. If you have more experience using Ghidra/IDA Pro you just need 2) so you can compare what changes between the three versions.

![imagen](https://i.imgur.com/3mKaS0Q.png)

2. Right click on the game again and click on Extract Data ->  ExeFS. Select a folder where you want to save these files and wait until it’s done. Then close Ryujinx. You no longer need it for the rest of this guide.

![imagen](https://i.imgur.com/0yVpaDj.png)

### Getting the nsobid/BID

You got a [video explanation here](https://youtu.be/d1XWoEgAgrU)

You can also get the nsobid as I show in [this video](https://youtu.be/i3l_xezcaKw?si=QCgBn4ek9eWpDZ0S&t=37). This video is focused on how to verify your files to know if there's something wrong (corrupted base game, update, corrupted files ...) but what you're looking for is at min 0:37. What you need is the BuildID letters and numbers.

![imagen](https://i.imgur.com/qHoL0Cp.png)

Finally, you can use [Tinfoil](http://tinfoil.io/Title/). Search the game, in this case [Zelda TOTK](http://tinfoil.io/Title/0100F2C0115B6000). Now scroll down until you see the Build ID's section. Get all numbers and letters. Don't include the 0s at the end, we don't need them. **Keep in mind that sometimes Tinfoil may not have updated the BID**. If this is the case, just use NSCBuilder or HxD. 

### Things to keep in mind when you use NSCBuilder/NxFileViewer

[NSCBuilder](https://github.com/julesontheroad/NSC_BUILDER/releases) needs your `prod.keys` to be able to work. 

So you'd to open the NSCBuilder folder, then go to `ztools` folder and open it. Now do a copy of your prod.keys and rename it to `keys.txt`. 

Finally drag your `keys.txt` into the `ztools` folder and you're done. NSCBuilder should works now.

On the other hand, [NxFileViewer](https://github.com/Myster-Tee/NxFileViewer/releases) needs a `.switch` folder that will be located in the folder  where you have your Downloads, Documents, Videos, Music Folder etc etc.

In my case it's `C:\Users\Stevens`

You probably don't have this folder, so create it and **name it .switch**

Now open it and paste your prod.keys there. NxFileViewer should works now.

[CLICK HERE](https://youtu.be/jTJYpuG-9Ek?si=ZlOh9_rA2muqoj4C) for a quick video about how to port/update the mods (This method might not work all the time) 

[CLICK HERE to continue with the guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/SetupGhidra.md)
