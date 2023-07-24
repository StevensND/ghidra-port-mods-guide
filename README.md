# How to port .pchtxt (ExeFS) Switch Mods from a previous udpate to a newer update. Mainly focus on emulators (Yuzu/Ryujinx)

### What we will need:

- [Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases)
- [SwitchLoader Extension](https://github.com/StevensND/Ghidra-Switch-Loader/releases)
- [Java JDK](https://adoptium.net/temurin/releases/?version=20) I suggest you the latest version: Java JDK 20
- [Ryujinx](https://ryujinx.org/download/) to extract the ExeFS files. You can do it with Yuzu too but IMO Ryujinx do a better job and it’s more faster
- [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20) or any other Hex Editor like [this one](https://hexed.it/) (online version)
- [NotePad++](https://notepad-plus-plus.org/downloads/) It's not really necessary but IMO it's more convenient compared to Windows Notepad
-	**Previous game update** (I suggest you at least 2 previous updates). This is just for starters. As son as you gain experience with Ghidra you will only need the previous version and the new version you want to update/port. So in my example would be: TOTK 1.1.1 + 1.1.2 + 1.2.0. However for the guide I will only use TOTK 1.1.2 + TOTK 1.2.0
-	**Latest** game update (In this case TOTK 1.2.0).
-	**Second Monitor/Ultrawide Monitor**: This is just a suggestion. It's not really necessary but it makes your job easier. You will be searching and getting data from one version that you will then need to search in the new version. So you will have to split the screen: On the left one version and on the right the other version.
-	**Time + a lot of patience**: Some games take less time to analyze with Ghidra (depending on the weight of the original game and the update, the changes incorporated etc etc).

  If you don't have much time I would recommend starting with a game like ...  ToZ: Link's Awakening. You can find the [mods here](https://yuzu-emu.org/wiki/switch-mods/) (Press Control F on your keyboard and search for Awakening).

  [CLICK HERE TO START the guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/RyujinxSteps.md)

  # Special Thanks to:

  [Father Of Egg](https://www.reddit.com/user/Father_Of_Egg) for teaching me how to use Ghidra + basic concepts.
  [PixelKiri](https://www.reddit.com/user/PixelKiri) for update SwitchLoader and make it compatible with latest Ghidra updates.
  [ChanseyIsTheBest](https://gbatemp.net/members/chanseyisthebest.608269/) for GBATemp tutorials
  [Fruithapje21](https://www.reddit.com/r/totkmods/comments/149lpz5/comment/jriqx7f/?context=3) for Aspect Ratio GDB + Ghidra Guide
