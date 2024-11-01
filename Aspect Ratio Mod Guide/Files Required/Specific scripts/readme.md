Here you will find scripts that you should use for some specific games such as Mario Kart 8 Deluxe.

The reason for using these scripts instead of the normal `3.GDBtoGHIDRA.py` script is:

## Mario Kart 8 Deluxe

Some games don't use `7100000000` as Base Address.

Mario Kart 8 Deluxe use `60000000` instead of `7100000000` so if you use the `3.GDBtoGHIDRA.py` normal script you would not get a working Ghidra Address.

## Super Mario Party Jamboree

>[!TIP]
This change should also be applied to games such as **Shadows of the Damned: Hella Remastered** and **Nikoderiko: The Magical World**

If you use the `monitor get info` command on GDB, you'll notice that on the `Modules` section you will get something like this:

```
Modules:
  0x0080000000 - 0x0080003fff nnrtld
  0x0080005000 - 0x0083ab5fff Game.nss
  0x0083ab6000 - 0x0084db4fff glslc
  0x0084ddc000 - 0x008533dfff multimedia
  0x008545c000 - 0x0085f60fff nnSdk
  ```
We will focus on `0x0080005000 - 0x0083ab5fff Game.nss`

Usually **the script and most games use** `0x0080004000` instead of `0x0080005000`

So we will need to replace the script (edit it with Notepad or Notepad++), replace that line with that value and save the script. 

![imagen](https://i.imgur.com/OoCWkDf.png)

Finally run the script again and you should get the right offset for Ghidra.

Anyway, I leave the modified script in a .zip file