# Setup

Unfortunately I cannot give you a download link for [IDA Pro](https://hex-rays.com/ida-pro/). This software is a **paid software**

In order to analyze our main file (ExeFS) extracted from Ryujinx we will need the loader/script `nxo64.py`

You can find it [here](https://github.com/reswitched/loaders/blob/master/nxo64.py)

Just click on the arrow icon (Download Raw File) and get it.

You can also click on the icon to the left (Copy Raw File). Now open NotePad++ and paste it. Finally save it as `nxo64.py`

# Where to place nxo64.py

Once we have the `nxo64.py` file we will have to open our IDA installation folder and locate the `loaders` folder.

Here we will paste `nxo64.py` and that's all.

![image](https://i.imgur.com/ggMmtDy.png)

# Running IDA

The first time we run IDA we will see this:

![image](https://i.imgur.com/VPbQRa3.png)

Just click on `GO`. Now you'll see the IDA interface and a text saying: `Drag a file here to disassemble it`

Locate your `main` file and drag it there.

You'll see this screen. **Don't touch** or change anything. Just click on `OK`

![image](https://i.imgur.com/56jjzoj.png)

Another message will appear. Just click on `Yes`. After this another warning message will appear. Click on `OK`

![image](https://i.imgur.com/iTnfLNl.png)

Now IDA will start analyzing the main file of the game. Wait until it says `idle`.

![image](https://i.imgur.com/RIHrZvj.png)

We're done. Finally, learn the following [shortcuts](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/IDA/Shortcuts) to know how to use IDA.