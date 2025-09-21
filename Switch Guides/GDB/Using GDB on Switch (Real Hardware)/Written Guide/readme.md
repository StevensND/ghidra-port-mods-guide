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

`500` is **1280 in Hexadecimal**. You can check this info in [this website](https://www.rapidtables.com/convert/number/hex-to-decimal.html?x=500)

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

Now it's time to move to Ghidra. **I WILL NOT EXPLAIN HOW TO SETUP GHIDRA IN THIS GUIDE**. You can have this info in [THIS LINK](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/SetupGhidra.md)