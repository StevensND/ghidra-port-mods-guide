## Things that you should do and check before continue

At this point I suggest you [open the following link](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md) in a new tab or window. You will need to check it out to understand the following steps as well as to be able to use Ghidra.

**Please, extract the ExeFS files and get the nsobid/BID**

Then continue [setting up Ghidra](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/SetupGhidra.md)

**Remember to analyze the main file** extracted from the ExeFS files using Ghidra. Otherwise, you can't continue with the guide.

## Some notes. Take a look at them

> [!TIP]
Maybe instead of using this script you want to use another script for a specific game.

>[!NOTE]
Take a look at the [specific scripts section](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Aspect%20Ratio%20Mod%20Guide/Files%20Required/Specific%20scripts) for some games

>[!IMPORTANT]
The reason for using these scripts instead of the normal `3.GDBtoGHIDRA.py` script is that **some games don't use `7100000000` as Base Address**. You will know the Base Address of the game that you are using once you have analyzed the entire `main` file.

>[!CAUTION]
Games like Mario Kart 8 Deluxe use `60000000` instead of `7100000000` so if you use the `3.GDBtoGHIDRA.py` script you would not get a working Ghidra Address.

# Running our last script: 3.GDBtoGHIDRA.py

We have now reached our last step, where we will simply run this script. 

Once we run it we get the following message:

```
Enter GDB address
```

Here we copy our GDB Address, in this case: `0x829b9108` and that's all. The script returns this message:

```
Enter GDB address: 0x829b9108
Ghidra Address: 71029b5108
```

In this case I have used this GDB Address because I know that `71029b5108` in Mario Wonder is an Address that modifies both the AR in the levels as well as in the Overworld.

Otherwise I would try using something like `0x802bdfe8` and change the instruction in Ghidra/IDA. Then I would see what happens in the game etc etc.

## IDA PRO

I have decided to separate IDA and include it in another section. So [click here if you are going to use IDA](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Aspect%20Ratio%20Mod%20Guide/Steps/GDB%20to%20IDA.md)

## Ghidra

So ... this is Ghidra:

![image](https://i.imgur.com/cCPcWvW.png)

What I did was press the G key on the keyboard and type `71029B5108` to go directly to my offset to explain this example.

As you can see I got two XREF: FUN_71002b9614 and FUN_710069e47. 

One modifies the overworld and the other modifies the AR in the level I am playing. 

However `71029b5108` modifies this at the same time.

## What you should do now

On May 2, 2024 I add this next info since from this moment, users following this guide were copying literally what I was doing instead of trying to understand the guide and the explanation.

So ... Let's go back to the screenshot again:

![image](https://i.imgur.com/cCPcWvW.png)

**Remember that in this case we got two XREF: FUN_71002b9614 and FUN_710069e47**. 

Click on one of them, for instance XREF: FUN_71002b9614.

I've this result:

![imagen](https://i.imgur.com/t7A8bRV.png)

From here **we will focus on all values starting with s** (s0, s1, s2, s3 ...) and start testing our mod.

Keep in mind that from this point on it's all trial and error, so finding the right offset may take some time and may not be as fast as you expected.

For instance, I could take `71002b9fc8` and start writing my mod. The full line is:

`71002b9fc8 01 10 2c 1e     fmov       s1,0x3f000000`

I could change `fmov s1,0x3f000000` and convert it to: `fmov s1, #2.375` using [ARMConverter](https://armconverter.com/)

## Writing my mod code

I assume that you have already extracted the main file (ExeFS) and have Ghidra set up + analyzed the main in Ghidra as I advised you before starting these steps.

Now, all you've to do is open your emulator and open your mods directory folder. 

Once this mods directory folder is opened, in the same directory, create a new folder.

Call it `Test` and inside this Test folder create another folder called `exefs`.

Inside this exefs folder, create a text file and call it whatever you want ... for example: 1.0.2. **Make sure that the file extension is .pchtxt**.

You can create a file with a .txt extension and then change the extension to .pchtxt by changing the file name and extension.

Open this .pchtxt file and use the following info as a template:

```
@nsobid-F91868B88F60D3D59009DB3389FDE314A6A32FCD

# Super Mario Bros. Wonder [010015100B514000] v1.0.1 - 21:9 Aspect Ratio

@flag print_values
@flag offset_shift 0x100

// 21:9 Aspect Ratio

@enabled
029B5108 54551540
@stop

@StevensND
@KeatonTheBot

https://linktr.ee/stevenssv2
https://linktr.ee/keatonthebot
```

Here you MUST change the nsobid (you should already know how to get it beforehand), also change the next line starting with #. Type the name of the game for which you are making the mod , TitleID, version, what mod it is etc etc.

Keep the following lines:

```
@flag print_values
@flag offset_shift 0x100
```

Re-write what the mod is about and **the most important thing to change starts from @enabled**

Write the final offset you have obtained from Ghidra and then the instruction.

In our example it would be something like this:

`002B9FC8 0170201E`

0170201E = fmov s1, #2.375. Remember to use the [ARMConverter site](https://armconverter.com/) to obtain the 0170201E result or similar result.

And that's all. Take another look at the template if you've doubts and finally: test your mod. 

If it works and changes the aspect ratio, that would be all, if not, you would have to keep trying offsets and instructions until you find the expected result.

## What I did for this Mario Wonder Aspect Ratio Mod (only useful in this game)

Let's go back to the screenshot again:

![image](https://i.imgur.com/cCPcWvW.png)

I right-clicked on `71029b5108` and then go to `Data` and click on `Float`. Now we see this info: `float 1.777778`. Save (Press Control S)

Do you remember when I searched for `1.77777802` instead of `1.777777791` or `1.777777777`? ... Well, it was because of this.

Now ... how do I know the float value of other ARs other than 16:9, 21:9, 16:10 or 32:9?

Simply divide ... 16/10 = 1.6, 21/9 = 2,3333 ...

Now go to the [ArmDeveloper site](https://developer.arm.com/documentation/ka001136/latest) and check the table ...

In this case 21/9 = 2,3333 ... However 2,3333 is not in the table. It's between `2.25000000` and `2.37500000`

You have to take the nearest or closest value, in this case `2.375`. But in the case of Mario Wonder, we need the true float, which in this case is `2.33333333`.

Right click on `71029b5108` and then go to `Patch Data`. Tpye `2.33333333` and Press Enter. Now the bytes should changed to: `54 55 15 40`

So our mod will be:

```
@nsobid-F91868B88F60D3D59009DB3389FDE314A6A32FCD

# Super Mario Bros. Wonder [010015100B514000] v1.0.1 - 21:9 Aspect Ratio

@flag print_values
@flag offset_shift 0x100

// 21:9 Aspect Ratio

@enabled
029B5108 54551540
@stop

@StevensND
@KeatonTheBot

https://linktr.ee/stevenssv2
https://linktr.ee/keatonthebot
```

**But what happens if I got something like this?:**

```
71002b9fcc ldr s3,[x8, #0x108]
```

In this case I would use [ARMConverter](https://armconverter.com/?code=fmov%20s3,%20%232.37500000) and modify that instruction to: `fmov s3, #2.37500000`.

When we have/want to do fmov, we normally look at the values in the table. So our final code would be:

```
002B9FCC 0370201E
```

# Yuzu or Ryujinx Settings

![image](https://i.imgur.com/AYKXx0l.png)

Remember that in order to use the Aspect Ratio mods we have to modify our Aspect Ratio in our game custom settings. 

To do this we will `Right click on the game` and then click on `Properties`. We will go to the `Graphics` section and finally we will locate the `Aspect Ratio` section. 

Set it to `Stretch to Window`

For Ryujinx we will do the same. Click on `Options` and then click on `Settings`

Click on `Graphics` and finally locate the `Aspect Ratio` section. Set it to `Stretch to Fit Window`

![image](https://i.imgur.com/AmS0XpG.png)

# Clean Files

Once you have finished the guide and made the mod: I suggest you delete all generated .txt files including `gdb.txt` from the `bin` folder.

**Before do this**: Backup all the things that you consider important info.

So you would have to delete: `gdb.txt`, `mappings.txt`, `watch_script.txt` and `Ghidra_Offset.txt` from the `bin` folder.

We will do this to avoid possible conflicts the next time we want to repeat the guide.

# Final Tips

Press S key (Search Memory), select Hex and then type our value in Hexadecimal/Hex (0x3fe38e3b). Then click on Search All.

![image](https://i.imgur.com/7ef8geC.png)

0x3fe38e3b (Hex) = 1.77777802 (Decimal).

You can use the [Floating Point Converter site](https://www.h-schmidt.net/FloatConverter/IEEE754.html) to get this value.

![image](https://i.imgur.com/7c73OOj.png)

In case [we find something (please, click on this link to know what I'm talking about)](https://i.imgur.com/SFmMOPF.png) we would only have to follow the last steps **(check the What you should do now + Writing my mod code)** sections again to give an instruction to the offset/address and that's it.

Otherwise, go to `Analysis` -> `One Shot` and click on `Aggressive Instruction Finder`.

**Remember to do all of this only when you have finished analyzing the main file**. Wait for it to finish: look at `undefined (1)` text.

You will know that it's over when you see undefined (1) at the bottom right and no more analysis is being done

![imagen](https://i.imgur.com/WtpFX1M.png)

Sometimes by doing this we can find debug symbols that were hidden before.

We can also go to `Search` and click on `Program Text`.

Search for: Here we would type our value in Hex. Then click on All Fields, All Blocks and finally on Search All.

This will take a long time, but it's an alternative in case we have not found anything in CE and GDB.

# End of the guide

That's it, that's the end of the guide. From here on it's just a matter of testing and discovering that each value you have chosen changes according to the instruction you have given it.

I hope it has been useful.

If you have any doubt about the script or if something is not working right ask me or ask Flash in Discord:

`stevenss.` in my case, `fl4sh_` in the other case.