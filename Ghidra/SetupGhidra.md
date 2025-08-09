# How to setup Ghidra

**DISCLAIMER**: "->" means click on

1.	[Download Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases). Unzip it. Open the unzipped folder and search for ghidraRun.bat (if you don’t know how to see files extensions go to the top of your folder tab and then click on View. Then click on Extensions checkbox). Run ghidraRun.bat.

![imagen](https://i.gyazo.com/204fc945610c663fedfc4c3d0741bc7c.png)

2.	Get [SwitchLoader](https://github.com/StevensND/Ghidra-Switch-Loader/releases) and place it somewhere you can find it easily. Don’t unzip it. It’s not neccesary. Remember to install Java JDK too.

> [!NOTE]
If you want to know how to compile Switch Loader on your own PC, [HERE'S THE VIDEO TUTORIAL](https://www.youtube.com/watch?v=qZl6JnniSxo)
   
3.	On Ghidra click on File -> Install Extensions and click on the "+ icon". Search for the .zip file (SwitchLoader) and click on OK and install it. It should look like this:

![imagen](https://i.imgur.com/yP6sQ04.png)

4.	Create a project: Click on File -> New Project. Click on Next and then select where you want to save your project. Put a name's project and click on Finish.
   
5.	I suggest you create a New Folder (Right click -> New Folder). We will do this to better organize ourselves. You can create a general folder called "TOTK" for example and then subfolders according to the version we are going to use. This will also allow us to open several Ghidra tabs. Otherwise we will only be able to have 1 tab open.

![imagen](https://i.imgur.com/B0Wx1U4.png)

Once you have everything set up, **find the folder** where you extracted the ExeFS files and **drag the file named main** to the corresponding folder. A window will pop up (this is the SwitchLoader extension). Just accept and continue.

Now open the corresponding main in Ghidra. The first time you will get a window asking to analyze the code. Analyze it. A new popup window will appear. Leave all options as they are by default and **Enable (Switch) IPC Analyzer too**. Finally click on Analyze.

**If you didn't see the pop-up window** asking you for analyze or if you closed it by mistake or clicked No, **go to Analysis** (next to File and Edit) and **click on Auto Analyze**. Alternatively you can directly press the "A" key on your keyboard.

![imagen](https://i.imgur.com/skB2aHK.png)

**Remember to Enable (Switch) IPC Analyzer too**. Let Ghidra analyze the file (as I said before this may take a little or a lot of time depending on the game and the update) so do something else in the meantime and be patient. 

Also **Disable Non-Returning Functions - Discovered** option: This takes a lot of time for no benefits in game reverse engineering.

> [!TIP]
You can save this profile by clicking on Save. Give the profile a name and that's all. After that, you can select the profile by *clicking on the arrow next to the Delete Button*.

Look at the screenshot if you have doubts.


> [!NOTE]
You will know that it's over when you see undefined (1) at the bottom right and no more analysis is being done. 

**PLEASE ANALYZE ALL THE MAIN FILES REQUIRED before proceeding**. For the next steps I assume you have already done this.

![imagen](https://i.imgur.com/WtpFX1M.png)

[CLICK HERE to continue with the guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/GhidraSteps.md)

## UNREAL ENGINE TIPS

> [!TIP]
If we're going to analyze Unreal Engine games sometimes we want to search for stuff like `r.BloomQuality` or `r.DepthOfFieldQuality` 

In this example I'm going to analyze Crash Bandicoot 4: It's About Time

By default, **Ghidra won't find this** so here are the steps that we need to do to setup the search:

1. Go to `Search` and then click on `Memory` or just press the `S key` on your keyboard.

This will open the following tab.

![imagen](https://i.imgur.com/M4R3ZcO.png)

2. Move your mouse over the icons until you find the one that displays the next info: `Toggles showing the search options panel`

This icon is the one selected with the red square. You will see the following panel.

![imagen](https://i.imgur.com/a7Ta3Iv.png)

3. Click on the first square next to the `r.DephtOfFieldQuality` text and change that to `String`

If I remember correctly, by default this square is set to `Hex`. **It must be String so change it**

4. Focus and move your mouse to the `String Options`. Here, **you have to change the Encoding**

By default is set to `US-ASCII`, so change it to `UTF-16` 

5. Do the search and now you will find the desire result.

> [!NOTE]
If you still don't find anything try to change it to other option and repeat the search until you find something.

