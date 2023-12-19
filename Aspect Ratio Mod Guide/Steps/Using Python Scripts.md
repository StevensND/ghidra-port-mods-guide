# DISCLAIMER

Before I start with this part, **I wanted to thank Fl4sh_#9174 or simply fl4sh_** 

He's a Discord user who messaged me and shared the scripts for testing.

For this reason you have this guide. He and I have tried other non-Zelda TOTK games such as Mario Wonder, Persona 5 Tactica, Dragon Quest Monsters, Sonic Frontiers, Sonic Superstars, Mario Party ... among others and we have been successful in modifying the Aspect Ratio.

However in games like Master Detective Archives Rain Code and Demon Slayer, I at least, have not been successful. The Aspect Ratio doesn't change and the image becomes smaller (as if cropped).

# Running our first script: Flashscript V2.py

We will go back to our gdb-multiarch folder, locate the `bin` folder and then locate our scripts, which in this case are 3.

We will start with the first one: `1.Flashscript V2.py`. As soon as we open it we will see the following message:

Type or Paste the MONITOR GET INFO text or the ADDRESS RANGE that you want to search for and press Enter (0x0000000000 - 0xffffffffff scan everything).

Go back to the gdb-multiarch console and press Control C on your keyboard (this function is known as quit). 

You will see a bunch of messages indicating `New Thread` as well as a message similar to:

```
Thread 1 "MainThread" received signal SIGTRAP, Trace/breakpoint trap.
0x00000000837a8084 in ?? ()
```

Now we can type or paste commands. In this case, we will paste these 2:

```
monitor get mappings
monitor get info
```

Paste them 1 by 1. The first command will take a while but once it's finished you will be able to paste the second one.

Save the information you get from `monitor get info` as this is what we need for our first Python script.

In my case it's:

```
  Alias: 0x1104600000 - 0x21045fffff
  Heap: 0x2104600000 - 0x23045fffffff
  Aslr: 0x0008000000 - 0x7fffffffffff
  Stack: 0x1084600000 - 0x11045fffffff
Modules:
  0x0080000000 - 0x0080003fff nnrtld
  0x0080004000 - 0x0083648fff Secred.nss
  0x0083649000 - 0x00843a0fff nnSdk
```

These are all the regions into which the game is divided. 

I will take the following information and paste it into the script:

```
0x0080004000 - 0x0083648fff Secred.nss
```

I do this because I know that the value that I'm looking for is in that region. Otherwise, I would do like you and search all regions, i.e. paste the following:

```
0x0000000000 - 0xffffffffffffffffffff
```

When you do this it will give you many values and GDB will take longer to find the GDB Address you need.

Don't be alarmed and be patient. It's better to do it this way.

So we paste the information into our script and press Enter. If the script does nothing, press Enter again.

![image](https://i.imgur.com/IQgLx3N.png)

The next message in my case will be:

```
Address range:
0x0080004000 - 0x0083648fff
Press Enter to execute the second script...
```

So Press Enter again and we will get this message:

```
Enter the address ranges separated by commas (e.g., 0x0080004000 - 0x0081c45fff, 0x2103c00000 - 0x2303bfffff)
```

Grab and paste the `Address range` that the script gave us. In my case: `0x0080004000 - 0x0083648fff` and Press Enter.

The next message is: 

```
Enter the Hexadecimal Representation value that Floating Point Converter gave you and Press Enter (e.g. 0x4091c71c)
```

Now go to the [Floating Point Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html) website and type the value that you leave on CE. In my case: 2.377777815

Floating Point Converter will return this value converted to Hex. In this case: 0x40182d83

Here's a list of other values:

```
0x3fe38e39 = 1.777777791
0x40182d83 = 2.377777815
0x4091c71c = 4.555555344
```

Paste `0x40182d83` and press Enter. This is our last message. You will probably have more finds than me. After this, we can Press Enter and the script will close:

![image](https://i.imgur.com/FVckq6l.png)

Now we will go back to our gdb-multiarch folder and again locate the `bin` folder. 

Once located, locate a file named `mappings.txt`. Open this file and you will find something like this:

```
find 0x80004000, 0x82015fff, 0x40182d83
find 0x8320d000, 0x83648fff, 0x40182d83
find 0x80004000, 0x83648fff, 0x40182d83
find 0x82016000, 0x8320cfff, 0x40182d83
```
Paste this into the gdb-multiarch console and wait for it to finish. 

![image](https://i.imgur.com/Qtgb7L3.png)

You will know you are done when GDB finds no more results and you can delete or type again.

In my example, GDB has found the following:

```
(gdb) find 0x80004000, 0x83648fff, 0x40182d83
0x829b9108
1 pattern found.
```

`0x829b9108` is the GDB Address I was looking for all this time. 

If you have not been paying attention to the GDB console, an easier way to locate this address is by opening the `gdb.txt` file located in the `bin` folder. 

Open that file and then press Control F (if you're using NotePad++) or Control B (if you're using NotePad) and search for your last 3 digits. In my case: 108.

Keep searching until you find something like the info below. I found this:

```
Pattern not found.
Pattern not found.
0x829b9108
1 pattern found.
Continuing.
```

As you can see, this address was between 

```
  0x0080000000 - 0x0080003fff nnrtld
  0x0080004000 - 0x0083648fff Secred.nss
```

How I knew this?. Just look at the find line:

```
find 0x80004000, 0x83648fff, 0x40182d83
```
In this command the first two 0s have been ignored, going from `0x0080004000` to `0x80004000` and from `0x0083648fff` to `0x83648fff`.

Just try to locate the address found in the game regions if you need to search for this address again. It will save you a lot of time.

# Running our second script: ScanGDB.py

We go back to the `bin` folder and run the second script: `2.ScanGDB.py`. We will see the following message:

```
Type or Paste the final value (e.g. 0x829b9108) that GDB found (press Enter for all addresses, type 'exit' to quit)
```

Here we paste `0x829b9108` and we will Press Enter.

In the `bin` folder a new file named `watch_script.txt` will have been generated. We will open it and we will find the following information:

```
set *0x829b9108 = 0x4091c71c <<change it and check if it changes on CE>>
awatch *0x829b9108 <<set the watchpoint>>
```

We copy the first line, i.e. the set line, and paste it into our GDB console. 

Then press the C key and check that the Aspect Ratio has been changed both in the game and in Cheat Engine.

As you can see in [this image](https://i.imgur.com/JsTH7L5.png) the CE value changed as well as the AR in the game.

In this way we have ensured that this address is correct and that when we change the value, it will change both in CE and in the game.

You can test by putting a random value in Floating Point Converter such as `1.23456789` and get that value in Hex. 

Then you would do: 

```
set *0x829b9108 = 0x3f9e0652
```

And you would check that the values and the AR have changed. Finally go back to GDB, Press Control C and paste the last line, the awatch line and press Enter.

You will get this message:

```
(gdb) awatch *0x829b9108
Hardware access (read/write) watchpoint 1: *0x829b9108
(gdb)
```

Press C and then press Enter. You will get this message:

```
(gdb) c
Continuing.
[Switching to Thread 119]

Thread 44 "BaseProcExecutor0" hit Hardware access (read/write) watchpoint 1: *0x829b9108

Value = 1083295516
0x00000000802bdfd0 in ?? ()
(gdb)
```

Now paste this command: `x/20i $pc-40` and press Enter. You will see something like this:

![image](https://i.imgur.com/rE0nUIW.png)

Copy all this information into another text file because it will be the information you will need for our final step.

Now, Press Control C again and keep spamming C and Enter until 0x00000000802bdfd0 in ?? () is repeated again. Copy and paste all information that is not repeated.

# Clarifications before proceeding to the final step

First of all, **I want to go back to this info**:

```
(gdb) awatch *0x829b9108
Hardware access (read/write) watchpoint 1: *0x829b9108
(gdb)


Press C and then press Enter. You will get this message:


(gdb) c
Continuing.
[Switching to Thread 119]

Thread 44 "BaseProcExecutor0" hit Hardware access (read/write) watchpoint 1: *0x829b9108

Value = 1083295516
0x00000000802bdfd0 in ?? ()
(gdb)


Now paste this command: `x/20i $pc-40` and press Enter.
```

**This step is very important and you may be confused**, so I want to clarify it:

In my **Mario Wonder example**, `0x829b9108` would be the GDB address that I'll be using for the last script since it's the value that GDB found when using the `find` command. However, **YOU DON'T HAVE TO USE THIS ADDRESS IF YOU'RE USING ANOTHER GAME**.

Once you have used the command `awatch *0x829b9108` and pressed Enter, you should `type C` and `press Enter` again. 

After this you would use the command `x/20i $pc-40` and press Enter.

You would copy the information it gives you in another .txt file and **repeat the process of typing C, press Enter and retype the command `x/20i $pc-40` and press Enter**.

**Let's look at a new example. This time it's Pokémon Let's Go, Eevee!**

The address found by GDB is: `0x2154cc2874` so what I would do is type the command: `awatch *0x2154cc2874` and `Press Enter`. After this I would use the command `x/20i $pc-40` as shown in the image below

![image](https://i.imgur.com/b3gxe41.png)

Now [I would copy that information into a new .txt file](https://i.imgur.com/KAGW7e9.png), retype C and press Enter again.

I would repeat the same thing again until the information was repeated. Once it repeats I stop.

![image](https://i.imgur.com/OVd71iX.png)

So **instead of using the GDB Address that GDB found earlier: `0x2154cc2874`, I would use something like: `0x803179a0` for the last script.**

![image](https://i.imgur.com/4WVevrm.png)

If I had used `0x2154cc2874` I would get this:

![image](https://i.imgur.com/n8Nprrg.png)

This won't work since Ghidra's Base Address usually is (**CAREFUL: NOT IN ALL GAMES**): `7100000000` and **in this case the script interprets that the base is: `9100000000`**

The Base Address for Mario Kart 8 Deluxe for example, would be: `60000000` instead of `7100000000`.

I hope this has clarified your doubts.

# End of Running our second script: ScanGDB.py

We are finishing. Before we continue I want you to focus on the image below:

![image](https://i.imgur.com/rE0nUIW.png)

Locate all the values starting with s (s1, s3 etc etc) as this is usually the instruction that changes the AR in Ghidra/IDA.

This is what we will proceed to do and change in the [final step](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Aspect%20Ratio%20Mod%20Guide/Steps/GDB%20to%20Ghidra.md).