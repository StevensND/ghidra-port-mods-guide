# Aspect Ratio Mod Guide

This guide is based on [u/fruithapje21](https://www.reddit.com/user/fruithapje21/) Reddit's  Guide that you can find [in this link](https://www.reddit.com/r/totkmods/comments/149lpz5/a_guide_on_how_to_create_asmpatches_for_nintendo/) and on the [old video guide](https://youtu.be/_lzU1HAasjo?si=TsgxtTBitjAoiCn1) that I did in the past.

However due to this method wasn't working for others games apart from Zelda TOTK, I have decided to redo the guide by modifying the method used by Fruithapje21.

The main issue was the "Cannot access memory at address ..." error while you were using the `set` command to check if the changes were working. Once you got this error, you couldn't continue and get the final address (the one you need for Ghidra/IDA to make the mod).

![image](https://i.imgur.com/e4ojT4l.png)

## Video Guide

If you wish, you can [check this new updated video guide](https://youtu.be/yV85AgYlE5c?si=7mA8F0ejHxNBmbds) while following all the steps of the written guide. 

## Requirements

- **[Python](https://www.python.org/downloads/)**: We're going to use Python scripts that will do the work for us and save us a lot of time. 

You don't need to have knowledge of Python but in order to use the scripts you need to have it installed.

- **[Ryujinx](https://ryujinx.org/download)**: We're going to use Ryujinx to extract the ExeFS files that we will analyze and use in Ghidra/IDA. 

If you don't know how to do it, please follow [this guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md). 

**Only** extract the ExeFS files of the **update you are going to use** for this guide.

**We will also need to know our nsobid**. This information as well as the necessary programs can be found in the **Ryujinx guide mentioned previously**.

- **[Yuzu](https://yuzu-emu.org/downloads/#windows)**: At the time of writing this guide, **only Yuzu is compatible with GDB**, so to use GDB we will need to use Yuzu too.

**I will not stop to explain how to set up Yuzu**, place keys, firmware, game directory etc etc. **I assume you already know how to do that**.

- **[Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases) + [SwitchLoader](https://github.com/StevensND/Ghidra-Switch-Loader/releases)**: We need Ghidra to make the mod. Please, read [this guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/SetupGhidra.md) to know how to setup Ghidra. 

I will skip the info about how to setup Ghidra in this guide.

- **IDA Pro + [nxo64.py](https://github.com/reswitched/loaders/blob/master/nxo64.py)**: IMO IDA it's more faster than Ghidra. If you're more familiar using IDA, then you need `nxo64.py`. Otherwise just use Ghidra.

My advice is to use Ghidra the first time to follow this guide and once you have everything clear or when you want to update the mod, switch to IDA. 

**IDA can be complex** and there are some options that I still don't know how to use/do using IDA. Otherwise as I said: just use Ghidra.

Check [this guide](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/IDA/Setup) to know how to setup IDA as well as the IDA shortcuts.

- **[Cheat Engine](https://www.cheatengine.org/)**: We need Cheat Engine to find the addresses that modify the Aspect Ratio of the game.

- **[Cheat Engine AD-Free](https://www.reddit.com/user/ChucksFeedAndSeed/comments/12usdd5/cheat_engine_75_adfree_installer/)**: Use this in case you don't want ads.

- **[GDB-Multiarch](https://static.grumpycoder.net/pixel/gdb-multiarch-windows/)**: Thanks to the combo of CE + GDB we will be able to find our final address for Ghidra/IDA as well as modify the Aspect Ratio in real time. So **using GDB is very important** for this guide.

I have also made a [GDB-Multiarch pack](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Aspect%20Ratio%20Mod%20Guide/Files%20Required) in case the link doesn't work, has been removed or is down. 

This pack (gdb-multiarch-13.2.zip) includes GDB-Multiarch and the Python scripts that we'll use.

## Pre-Setup

I assume that as of this moment you have already:

1. Installed Python.

2. Installed Ryujinx and configured Ryujinx. Extracted the ExeFS files using Ryujinx as well as having Yuzu installed and configured.

3. You have installed Ghidra, installed SwitchLoader, setup the options and finished analyzing the main ExeFS file.

4. Downloaded and installed Cheat Engine.

5. You have downloaded and extracted GDB-Multiarch.

So ... our **first step** will be open Cheat Engine.

Once Cheat Engine is open, go to `Edit` and click on `Settings`. Then click on `Scan Settings`.

Here focus on the section that says `Scan the following types of memory regions` and make sure to check the last checkbox: `MEM_MAPPED`. Finally click on `OK`

This is important to **be able to use Cheat Engine in Yuzu**.

![image](https://i.imgur.com/0uBe6Ue.png)

Now in our **second step** we will open Yuzu. 

Go to `Emulation` and click on `Configure`. Then click on `Debug`. Finally click on `Enable GDB Stub` and then click on `OK`

![image](https://i.imgur.com/LcUWQ1V.png)

> [!NOTE]
Be sure that you enable **EVERYTHING that I said** in the settings. Otherwise you're going to have issues and some things and scripts won't work.

**REMEMBER**: When you want to go back to play the game as you normally would, you will have to disable this option. Otherwise, **the game won't boot/run.**

We have finished with the Pre-Setup. Next I will give you some [important information](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Aspect%20Ratio%20Mod%20Guide/Info) that you need to know and keep in mind to make this mod, so open this link in a new tab.

## Credits

- **Fruithapje21:** Original guide.

- **Fl4sh_**: Python scripts.

- **KeatonTheBot**: ARMDeveloper link contribution as well as help to understand better some concepts.

- **StevensND**: New and update guide.

## Guide Start

Let's start with the guide. Click in [this link](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Aspect%20Ratio%20Mod%20Guide/Steps/Finding%20CE%20Values.md)
