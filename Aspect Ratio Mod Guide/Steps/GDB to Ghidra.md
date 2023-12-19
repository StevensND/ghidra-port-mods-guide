> [!TIP]
Maybe instead of using this script you want to use another script for a specific game.

>[!NOTE]
Have a look at the [specific scripts section](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Aspect%20Ratio%20Mod%20Guide/Files%20Required/Specific%20scripts) for some games

>[!IMPORTANT]
The reason for using these scripts instead of the normal `3.GDBtoGHIDRA.py` script is that **some games don't use `7100000000` as Base Address**.

For instance: Mario Kart 8 Deluxe use `60000000` instead of `7100000000` so if you use the `3.GDBtoGHIDRA.py` script you would not get a working Ghidra Address.

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

What I did was press the G key on the keyboard and type `71029B5108`

As you can see I got two XREF: FUN_71002b9614 and FUN_710069e47. 

One modifies the overworld and the other modifies the AR in the level I am playing. 

However `71029b5108` modifies this at the same time.

I suggest you right click on `71029b5108` and then go to `Data` and click on `Float`. Now we see this info: `float 1.777778`. Save (Press Control S)

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

But what happens if I got something like this?:

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

Press S key (Search Memory) and in Hex type our value in Hex (0x3fe38e3b). Then click on Search All.

In case [we find something](https://i.imgur.com/SFmMOPF.png) we would only have to follow the last steps to give an instruction to the address and that's it.

Otherwise, go to `Analysis` -> `One Shot` and click on `Aggressive Instruction Finder`.

**Remember to do all of this only when you have finished analyzing the main file**. Wait for it to finish: look at `undefined (1)` text.

Sometimes by doing this we can find debug symbols that were hidden before.

We can also go to `Search` and click on `Program Text`.

Search for: Here we would type our value in Hex. Then click on All Fields, All Blocks and finally on Search All.

This will take a long time, but it's an alternative in case we have not found anything in CE and GDB.

# End of the guide

That's it, that's the end of the guide. From here on it's just a matter of testing and discovering that each value you have chosen changes according to the instruction you have given it.

I hope it has been useful.

If you have any doubt about the script or if something is not working right ask me or ask Flash in Discord:

`stevenss.` in my case, `fl4sh_` in the other case.