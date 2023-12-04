This guide is mainly focused on how to update mods or cheats **for Yuzu or Ryujinx emulators**. It also includes some tutorials that you can use to start making your first mods in **exefs (IPSwitch)** format.

### What we usually need:

- [Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases) or IDA Pro
- [SwitchLoader Extension](https://github.com/StevensND/Ghidra-Switch-Loader/releases) if you're using Ghidra or [nxo64.py](https://github.com/reswitched/loaders/blob/master/nxo64.py) if you're using IDA Pro
- [Java JDK](https://adoptium.net/temurin/releases/?version=20). I suggest you the latest version: Java JDK 20
- [Ryujinx](https://ryujinx.org/download/) to extract the ExeFS files. You can do it using Yuzu too but IMO **Ryujinx does a better job and it’s more faster**
- [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20) or any other Hex Editor like [this one](https://hexed.it/) (online version)
- [NSCBuilder](https://github.com/julesontheroad/NSC_BUILDER/releases) to obtain our BID in a simpler way + your own `prod.keys`
- [NotePad++](https://notepad-plus-plus.org/downloads/) It's not really necessary but **IMO it's more convenient compared to Windows Notepad**
-	**Previous game update** (I suggest you at least 2 previous updates). **This suggestion is just for starters**. As son as you gain experience using Ghidra/IDA Pro you will only need the previous version and the new version you want to update/port. So in my example it would be: TOTK 1.1.1 + 1.1.2 + 1.2.0. However for the guide I will only use TOTK 1.1.2 + TOTK 1.2.0
-	**Latest** game update (In this case TOTK 1.2.0).
-	**Second Monitor/Ultrawide Monitor** (Optional): This is just a suggestion. It's not really necessary but it makes your job easier. You will be searching and getting data from one version that you will then need to search and locate in the new version. So in case that you only have 1 monitor, you will have to split your screen: On the left one version and on the right the other version.
-	**Time + a lot of patience**: Some games take less time to analyze using Ghidra (depending on the size of the original game and the update, the changes incorporated etc etc). Others, however, may take hours. In my case **I prefer to use IDA Pro and save a lot of time** (IDA is able to reduce Ghidra times by half or even less).

  If you don't have much time I would recommend starting with a game like ...  ToZ: Link's Awakening. You can find the [mods here](https://yuzu-emu.org/wiki/switch-mods/) (Press Control F on your keyboard and search for Awakening).

  [CLICK HERE TO START the Ghidra guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/RyujinxSteps.md)

### Other guides:

- [Converting cheats to .pchtxt guide](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Cheat%20to%20.pchtxt) | [How to update Switch mods or cheats using Interactive ASM Cheats Updater Video](https://youtu.be/jTJYpuG-9Ek?si=FfoiGiyC-uPgjxiA). These two guides are more or less related so I advise you to watch both for a better understanding.

# Special Thanks to:

- [Father Of Egg](https://www.reddit.com/user/Father_Of_Egg) for teaching me how to use Ghidra + basic concepts.
- [PixelKiri](https://www.reddit.com/user/PixelKiri) for update SwitchLoader and make it compatible with latest Ghidra updates.
- [ChanseyIsTheBest](https://gbatemp.net/members/chanseyisthebest.608269/) for GBATemp tutorials + [60fps mod tutorial](https://gbatemp.net/threads/how-to-make-60fps-ips-patch-for-nintendo-switch-game-ghidra-tutorial.625675/) + some useful [Python Scripts](https://github.com/ChanseyIsTheBest/NX-60FPS-RES-GFX-Cheats)
- [Fruithapje21](https://www.reddit.com/r/totkmods/comments/149lpz5/comment/jriqx7f/?context=3) for Aspect Ratio GDB + Ghidra Guide

If you want to say thanks for the guide and support me, here's my [Ko-Fi](https://ko-fi.com/stevenss)
