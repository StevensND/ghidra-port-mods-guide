### Goal/Objective of the guide

We want to be able to convert a cheat in .txt or .ips format to .pchtxt and make a mod (exefs in this case). This may or may not be useful depending on whether the cheat is often updated. There is really no need to have a mod in .pchtxt (exefs) if the cheat already exists.

Btw, here's more info about [Cheat Code Format](https://github.com/Atmosphere-NX/Atmosphere/blob/master/docs/features/cheats.md#cheat-code-format)

### Easy Steps

1. Get all files required [here](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Cheat%20to%20.pchtxt/Files%20Required)
2. Extract the ExeFS files as shown [here](https://youtu.be/d1XWoEgAgrU?t=78). We need the main file. Do this for the update in which the cheat was developed and another update as I told you in Files Required. If you need to know the BuildID, [check this](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md)
3. If the cheat is in .ips format instead of .txt: Drag the .ips file onto ips+pchtxt2cheat.py. It will automatically generate the .txt file you need.
4. Open the .txt file and you will see something like this:

![Screenshot](https://i.gyazo.com/9a290620fa370743b05b6547f944b39d.png)

Look at the structure. We have 3 columns. This is what we will call a "simple cheat".

- The **red colour** is what **allows the cheat to work** on real hardware/Yuzu or Ryujinx.
- The green is our Address
- The blue colour is the instruction we will give to the Address.

To convert the cheat to .pchtxt we will ignore the red colour and keep the rest. To make the mod work we will have to reverse the blue colour value using hexreverser.py ... So run hexreverser.py (Remember to have Python installed).

5. Type/copy & paste the value of the blue colour. In my case `1E204041`. If you have more lines starting with `040` keep entering values. Once you are done type "pause" and all results will be printed.

![Screenshot](https://i.gyazo.com/3b60ed2bb2206eaf0691e239e6ca8c15.png)

6. Finally do the exefs mod structure as I explained [here](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/GhidraFinalSteps.md): Get the nsboid etc etc and don't forget to place the mod into your mods folder directory.

### "Hard" Steps

The reason I call these steps "Hard Steps" is because this time we will use a more complicated cheat like this one:


```
[♯ 2. Inf. Health]
080E0000 02B0AFC8 176D734F F9400008
080E0000 02B0AFC0 B9000808 34000048
040E0000 02B0AFBC B9401808
040E0000 00667D04 14928CAE
```
This time we have 4 columns instead of 3. As before we will ignore the first column (080E0000 + 040E0000) and keep everything else. So ... steps:

1. Download Code Updater for Nintendo Switch and run `main_en.exe`

You'll see "Old Main File", "New Main File" and a Load Button. 

- Old Main File is to select the update in which the cheat was developed. In this case TOTK 1.2.0
- New Main File is for select the latest update/any other update. In this case we will select another update like 1.1.2. This doesn't really matter to us for now but the app doesn't work if the mains are not selected.

When you load the mains you may get an error. Just ignore it.

2. Copy the cheats and paste them on "Copy old cheats here" like [this](https://i.gyazo.com/c20919fddb36453ce7816459cf6d58c6.png) and click on Generate. You'll see an message saying: 080X0000 cheat codes have been splited into 04 and you no longer will see 080E0000 lines. This is totally fine.
   
 This will make updating this kind of cheats easier or making the mod in .pchtxt (exefs) easier due to we have the old structure that I explained before. My cheat would look like this:

 ```
[♯ 2. Inf. Health]
040E0000 02B0AFC8 F9400008
040E0000 02B0AFCC 176D734F
040E0000 02B0AFC0 34000048
040E0000 02B0AFC4 B9000808
040E0000 02B0AFBC B9401808
040E0000 00667D04 14928CAE
```
### What happened?

The first line: `080E0000 02B0AFC8 176D734F F9400008` has been splitted and converted to this two new lines: 
 
 ```
040E0000 02B0AFC8 F9400008
040E0000 02B0AFCC 176D734F
 ```

We have replaced 080E0000 by 040E0000 and divided our Address in 2: `02B0AFC8` (main address: this is the original address in `080E0000 02B0AFC8 176D734F F9400008`) and `02B0AFCC` (second address). The way we get `02B0AFCC` is by adding 4 to 02B0AFC8 (to do this use the Windows calculator in Programmer Mode and make sure to select Hex). So ... `02B0AFC8 + 4` = `02B0AFCC`

![Screenshot](https://i.gyazo.com/c937db3bbfbc61a5e556fa734111da76.png)

Keep in mind Windows calculator ignore 0's so if you miss one 0 just add it. The rest is done automatically by Code Updater for Nintendo Switch and makes it easy for you.

This will also be the case for all other lines starting with 080E0000. So next will be:

```
040E0000 02B0AFC0 34000048
040E0000 02B0AFC4 B9000808
```
And finally we have the lines that do not need to be split or converted.

```
040E0000 02B0AFBC B9401808
040E0000 00667D04 14928CAE
```


3. Finally do the reverse as I explained before, ignore `040E0000` and do the exefs mod structure as I explained [here](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/GhidraFinalSteps.md): Get the nsboid etc etc and don't forget to place the mod into your mods folder directory.

The mod should look similar to this:

![Screenshot](https://i.gyazo.com/b913ca68d725b4e2ea219520dc08c55b.png)

Do a test and check if it work or not and enjoy. If you want to update the mod in the future you can use Ghidra and follow this [guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md) or maybe try to use Code Updater for Nintendo Switch

**DISCLAIMER**: Code Updater for Nintendo Switch might not work all the time. Sometimes it can ignore and miss one line of the entire code or just ignore all the cheat and only make 1 change (for instance: you can't use Code Updater for Nintendo Switch directly to update/port cheats starting at 080E0000) so check if it's something missing. If you miss something update/port the mod using Ghidra
