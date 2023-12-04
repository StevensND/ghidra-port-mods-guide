### Goal/Objective of this guide

We want to update a .pchtxt mod or a cheat which is outdated to the latest version available using Code Updater for Nintendo Switch.

To do this, we will need to convert our .pchtxt or .ips file to a cheat format (.txt) and use Code Updater for Nintendo Switch to update it. Finally, we'll do the opposite: We will convert the cheat to .pchtxt format.

Btw, here's more info about [Cheat Code Format](https://github.com/Atmosphere-NX/Atmosphere/blob/master/docs/features/cheats.md#cheat-code-format)

### Steps

Before starting this guide, I suggest you read this other guide to better understand what we are going to do. Let's start:

1. Get all files required [here](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Cheat%20to%20.pchtxt/Files%20Required)
2. Extract the ExeFS files as shown [here](https://youtu.be/d1XWoEgAgrU?t=78). We need the main file. Do this for the update in which the mod/cheat was developed and another update as I told you in Files Required. If you need to know the BuildID, [check this](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md)
3. If the mod/cheat is in .ips format instead of .txt: Drag the .ips file onto ips+pchtxt2cheat.py. It will automatically generate the .txt file you need.

**DISCLAIMER**: If the mod/cheat is in .ips format and for some reason you need to convert it to .pchtxt use ips2pchtxt.py instead.

4. Open the .pchtxt file and you will see something like this:

![image](https://i.gyazo.com/fcd209d3937fc5b641c9d80106a39a1b.png)

Look at the structure. This is quite similar to what I explain in [step 1 of this guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/GhidraSteps.md).

To convert the .pchtxt to cheat we will have to reverse the `21008052 and C0035FD6` using hexreverser.py ... So run hexreverser.py (Remember to have Python installed).

5. Type/copy & paste the instructions. In my case `21008052 and C0035FD6`. If you have more lines keep entering values. Once you are done type "pause" and all results will be printed.

![Screenshot](https://i.imgur.com/GR6eyGB.png)

6. Now take a look at the following structure:

```
[60FPS]
04000000 | Address/Offset | Instruction
```

In my case, I will need to do this:

```
[60FPS]
04000000 03733FF0 52800021
04000000 00B83FF4 D65F03C0
```

Being `03733FF0 and 00B83FF4` my Offsets/Addresses and `52800021 and D65F03C0` the reversed instructions.

7. Now open Code Updater for Nintendo Switch.

You'll see "Old Main File", "New Main File" and a Load Button. 

- Old Main File is to select the update in which the mod/cheat was developed. In this case Master Detective Archives: Rain Code 1.0.0 (No Updates)
- New Main File is for select the latest update/any other update. In this case update 1.4.0 for the same game.

Paste your cheat into `Input Old Codes` and click on `Generate` wait until the cheat is updated and done and there you go, you have the cheat updated.

![image](https://i.gyazo.com/5addfe7595e7011b2e91fbe3c64f61fd.png) 

Now all you need to do is find the BID and create a new .txt file with the cheat inside this file and name it `BID`.txt

### Continue updating the .pchtxt mod

My old mod (mod for 1.0.0) had this structure:

```
@nsobid-58EA14313E7B5357FDF51E42B032CCB6

# Master Detective Archives: RAIN CODE [0100149019460000] v.1.0.0 - 60 FPS [US]

@flag print_values
@flag offset_shift 0x100

// 60 FPS US Version 

@enabled
03733FF0 21008052
00B83FF4 C0035FD6
@stop

@StevenssND
https://www.reddit.com/user/StevenssND
https://gbatemp.net/members/stevensnd.438828/
```

8. So now, I'd need to get the updated nsobid and replace the offsets/addresses that I got. The final updated mod will be:

```
@nsobid-B9E42653FB44EF2B8EEE7989FCCE1387

# Master Detective Archives: RAIN CODE [0100149019460000] v.1.4.0 - 60 FPS [US]

@flag print_values
@flag offset_shift 0x100

// 60 FPS US Version 

@enabled
03736970 21008052
00B45860 C0035FD6
@stop

@StevensND
https://linktr.ee/stevenssv2
https://github.com/StevensND/switch-port-mods
```

And that's all, mod updated using Code Updater for Nintendo Switch.

**KEEP IN MIND** Code Updater for Nintendo Switch not always works as expected. It may fail and freeze or crash or simply can't update the mod. Apart from this, keep in mind the structure of the cheats.

If your cheat is like: 

```
[60 FPS]
580F0000 0AB4E058
580F1000 00000018
580F1000 000000A0
780F0000 00000F14
640F0000 00000000 00000001
580F0000 0AB49108
780F0000 00000034
680F0000 00000000 00000000
580F0000 0B314540
780F0000 000007F8
640F0000 00000000 00000007
780F0000 00000004
640F0000 00000000 42700000
780F0000 00000014
640F0000 00000000 00000000
```

You can't update it using Code Updater for Nintendo Switch