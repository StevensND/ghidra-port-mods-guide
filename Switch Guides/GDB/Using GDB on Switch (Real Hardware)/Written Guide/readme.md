I'm going to [follow this guide](https://gist.github.com/jam1garner/c9ba6c0cff150f1a2480d0c18ff05e33) to explain this first step.

**You will also need to watch the [video guide](https://youtu.be/yYCi-7oRp2I?si=kuYSQImuTX-_O04U) while reading this guide.**

We will need to modify the `system_settings.ini` file to be able to use GDB.

This file is located in: `sd:/atmosphere/config/system_settings.ini`

Plug your SD card to your PC and locate this file.

![imagen](https://i.imgur.com/tzAlv82.png)

Do a backup of this file.  Now edit the original with Notepad or Notepad++ and locate the line starting with `[atmosphere]`

At the end of this line add the following:

```
enable_htc = u8!0x0
enable_standalone_gdbstub = u8!0x1
```

![imagen](https://i.imgur.com/XwyFdqW.png)

Save the file and replace it in your SD card path. Please, check that the file is edited and that it includes the new lines. 

**Otherwise, GDB won't work**.

Now turn on your Switch wait a while until everything loads. Now we will need to disable SaltyNX.

Open `Ultrahand/Uberhand` and go to `Sysmodules`. Then locate `SaltyNX` and press Y to turn it OFF. You must have a X icon saying OFF.

![imagen](https://i.imgur.com/MMPDC46.png)

>[!NOTE]
If SaltyNX is not disabled, you will get an error while trying to attach the game

After this, restart your Switch and wait until everyhing loads once again. After that, go to your PC and open GDB.

You have **ALL THE GDB COMMANDS** that we are going to need in [THIS LINK](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Switch%20Guides/GDB/Using%20GDB%20on%20Switch%20(Real%20Hardware)/GDB%20Commands)

Once GDB is open, you will need to type the following command line:

`set logging enabled on` and press Enter

Continue with the following line and press Enter, then continue with the next until you reach the last line:

```
set logging overwrite on
set architecture aarch64
target extended-remote YOUR SWITCH IP:22225
monitor wait application
```

![imagen](https://i.imgur.com/eWJEjU0.png)

Here you will see that GDB displays the following error:

```
Ignoring packet error, continuing...
```

Once this error appears in GDB, you should launch the game. In my case, Hollow Knight Silksong.

Now you will see that GDB shows a new message saying something like:

```
Send attach 0x8b to attach.
```

Type that into GDB and Press Enter. A new message will appear. Just type C and press Enter to continue.

![imagen](https://i.imgur.com/dmnCXay.png)

Load your save file. After that everything is loaded and you can move, go back to GDB and press Control C. 

**The game should freeze** and now you can type commands again.

![imagen](https://i.imgur.com/HUIaxZ9.png)

Type the following command:

```
monitor get info
```

Select the second option in modules in my case:

```
0x65f1206000 - 0x65f723ffff .elf
```

`0x65f1206000` is going to be our MAIN. Now, let's take a look to our cheat:

```
[720p Handheld - 1080p Docked]
580F0000 078883F0
780F0000 00008FE0
640F0000 00000000 00000000
```

`078883F0` is our `Cheat Address` and `00008FE0` is our `Jumpback Pointer Address`

>[!NOTE]
Remember that after every command, you must Press Enter

The next thing that we're going to type on GDB is `x/gx MAIN + Cheat Address` in our case that means:

```
x/gx 0x65f1206000+0x078883F0
```

This will give us the following result:

```
0x65f8a8e3f0: 0x000000065da06fc0
```
We will get `0x000000065da06fc0` and continue typing the next command `x/wx Result + Jumpback Pointer Address` in our case that means:

```
x/wx 0x000000065da06fc0+0x8fe0
```

This will give us the following result:

```
0x65da0ffa0: 0x00000500
```

`500` (Hexadecimal Value) is **1280 in Decimal**. You can check this info in [this website](https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=500)

>[!NOTE]
Remember that the default resolution for Docked is `1280x720`

Now get `0x65da0ffa0`. The next command that we will type is:

```
awatch *0x65da0ffa0
```

Now type C and press Enter. This will give us the following message:

```
Continuing.

Thread 1 "Thread_0x0000000000" hit Hardware access (read/write) watchpoint 1: *0x65da0ffa0

Value = 1280
0x00000065f3c8a9e0 in ?? ()
```

Now type `x/20i $pc-40` and Press Enter. This will give us a lot of results.

![imagen](https://i.imgur.com/7N9g09a.png)

Repeat the steps (Type C, press Enter. Type x/20i $pc-40 and press Enter) several times and check that you are having the same result.

>[!NOTE]
It's possible that in other cases and other games you will get new results.

If that's the case, just repeat the steps until the first result you obtained is repeated.

Now locate the Python script and edit it using Notepad or Notepad++

Find the line with the following info:

```
    # Mocked GDB information (replace this with actual GDB info) can be 0x0080004CD0 also
    gdb_info = {
        "Main.nss": "0x"
    }
```	

You will have to replace `Main.nss` with the MAIN that you obtained from `monitor get info` command. 

In this case:

```
"Main.nss": "0x65f1206000"
```

Now run the script. Copy the GDB result and paste it into the Python Script.

In our case it's `0x65f3c8a9e0`. Python script result will be `7102a849e0`

Now it's time to move to Ghidra. **I WILL NOT EXPLAIN HOW TO SETUP GHIDRA IN THIS GUIDE**. You can check this info in [THIS LINK](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/SetupGhidra.md)

Load the main and press G key to open the `Go To` tab. Type `7102a849e0` and click on OK. We will have the following function (Also we have the `UnityEngine.Screen::get width` string showed in the Ghidra Decompiler as a reference)

![imagen](https://i.imgur.com/I6UxGWt.png)

We need to focus in the following lines:

```
7102a849dc 14 55 40 29     ldp        w20,w21,[x8]
7102a849e0 89 00 00 35     cbnz       w9,LAB_7102a849f0
```
Here we need to know that a value is being “loaded” into w20 and w21.

To verify this, we can return to GDB and type the following command. **Thanks to Tashi for the info**

```
info registers $x20 $x21
```

That will give us the following result:

```
x20            0x500               1280
x21            0x2d0               720
```

So w20 loads `1280` and w21 loads `720` in Docked.

For the mod to work, **we will need to make a codecave**. This is an "advanced" step when making mods. 

Now focus on 

```
7102a849dc 14 55 40 29     ldp        w20,w21,[x8]
```

**We will need to patch this instruction**. However, before do this, we will need to do another step.

Press S on your keyboard. This will open the `Search Memory` Tab.

Check that is on `Hex` if you are using latest Ghidra version and then search for `1F 20 03 D5 1F 20 03 D5 1F 20 03 D5` bytes.

**1F 20 03 D5 means NOP**

![imagen](https://i.imgur.com/PVlmeP9.png)

We will have a lot of results. Now you've to check each result until you find a `RET` and 3 NOPS together.

![imagen](https://i.imgur.com/4NnZkcU.png)

My selected result is `71020D7464`. Select this one and press D on your keyboard. This will make the 3 NOPS appear.

![imagen](https://i.imgur.com/vtoAPKR.png)

Press G key to open the `Go To` tab and return to `7102A849DC`

Now it's time to patch the instruction. Click on the `ldp` area and then right click. Now select `Patch Instruction` or Press `Ctrl + Shift + G`

I suggest you watch the video guide around min 09:05 to know exactly what I'm doing.

I'm patching `7102A849DC` instruction with 

```
b 0x71020D7464
```

Now press G key and go back to `71020D7464`. You will need to patch `71020D7464` instruction with 

```
mov w20, #0x0
```

**Why I know is w20**

I explained this before: w20 loads `1280` and w21 loads `720` in Docked.

However if you remember the how to make the Resolution cheat we will only need one value due to **this game can change the resolution with just 1 offset/address and value** 

That's why I selected w20 only.

0x0 is `640F0000 00000000 00000000` in our cheat.

We will also need to patch `71020D7468` with 

```
b 0x7102A849E0
```

Now it's time to do the .pchtxt file. Our file will look like this:

```
@nsobid-DC3E4B892043EF2345C3EAF97A177E7C

# Hollow Knight: Silksong [010013C00E930000] v.1.0.28324 - 1080p Docked - 720p Handheld

@flag print_values
@flag offset_shift 0x100

// 1080p Docked - 720p Handheld

@enabled
02A849DC A24AD917 // b 0x71020D7464
020D7464 14008052 // mov w20, #0x0
020D7468 5EB52614 // b 0x7102A849E0
@stop

@StevensND
https://linktr.ee/stevensmods
https://github.com/StevensND/switch-port-mods
```

And that's all. However, [Fl4sh](https://github.com/Fl4sh9174) found a way to simplify this in this case, so you don't need to do a codecave. 

The mod will look like this:

```
@nsobid-DC3E4B892043EF2345C3EAF97A177E7C

# Hollow Knight: Silksong [010013C00E930000] v.1.0.28324 - 1080p Docked - 720p Handheld

@flag print_values
@flag offset_shift 0x100

// 1080p Docked - 720p Handheld

@enabled
02A84818 95000014
@stop

@StevensND
https://linktr.ee/stevensmods
https://github.com/StevensND/switch-port-mods
```

Now all you need to do it's convert this .pchtxt to .ips using [IPSwitch](https://github.com/3096/ipswitch/releases)

You can check [this video guide](https://youtu.be/m-V6Rs2sm9w?si=-_1Y49I89_tsxwUX) by Grown Up Gaming to know how to do this.

## Return everything to how it was before

Remember to remove the following lines in the `system_settings.ini` file to avoid possible issues:

```
enable_htc = u8!0x0
enable_standalone_gdbstub = u8!0x1
```

Save the file and replace it in your SD card.

**Also remember to enable SaltyNX again and restar your Switch**. Otherwise you won't be able to use Status Monitor and the overlays.

Having GDB and SaltyNX enabled also conflicts with Edizon or Breeze. For instance: you won't be able to save the cheat and you will have an error saying something like access denied.

## Updating the Silksong mod

If we want to update the Silksong mod, we will need to search for bytes.

**If we are using the Fl4sh suggestion**, then we will need to search for:

`e0 03 14 aa 00 01 3f d6 a0 12 00 36` then get `tbz`

**If we want to go for the codecave**, then we will need to search for:

`08 5c 40 f9 09 e4 40 b9 14 55 40 29` then focus on `ldp`. After that, search for new `NOPs` and finally do the codecave.

![imagen](https://i.imgur.com/Jy4BunG.png)

**Get the new nsobid** and replace the rest with the proper info, offsets/addresses and instructions.