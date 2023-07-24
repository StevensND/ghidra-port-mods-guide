# How to setup Ghidra

**DISCLAIMER**: "->" means click on

1.	[Download Ghidra](https://github.com/NationalSecurityAgency/ghidra/releases). Unzip it. Open the unzipped folder and search for ghidraRun.bat (if you don’t know how to see files extensions go to the top of your folder tab and then click on View. Then click on Extensions checkbox). Run ghidraRun.bat.
2.	Get [SwitchLoader](https://github.com/StevensND/Ghidra-Switch-Loader/releases) and place it somewhere you can find it easily. Don’t unzip it. It’s not neccesary. Remember to install Java JDK too.
3.	On Ghidra click on File -> Install Extensions and click on the "+ icon". Search for the .zip file (SwitchLoader) and click on OK and install it. It should look like this:

![imagen](https://github.com/StevensND/ghidra-port-mods-guide/assets/45856578/638c81b0-47e0-4ec2-816a-cb542af1d6a1)

4.	Create a project: Click on File -> New Project. Click on Next and then select where you want to save your project. Put a name's project and click on Finish.
   
5.	I suggest you create a New Folder (Right click -> New Folder). We will do this to better organize ourselves. You can create a general folder called "TOTK" for example and then subfolders according to the version we are going to use. This will also allow us to open several Ghidra tabs. Otherwise we will only be able to have 1 tab open.

![imagen](https://github.com/StevensND/ghidra-port-mods-guide/assets/45856578/1027f03c-5ba7-4a31-b674-ab4885b50312)

Once you have everything set up, **find the folder** where you extracted the ExeFS files and **drag the file named main** to the corresponding folder. A window will pop up (this is the SwitchLoader extension). Just accept and continue.

Now open the corresponding main in Ghidra. The first time you will get a window asking to analyze the code. Analyze it. A new popup window will appear. Leave all options as they are by default and click on Analyze.

Let Ghidra analyze the file (as I said before this may take a little or a lot of time depending on the game and the update) so do something else in the meantime and be patient. 

You will know it's finished when you see undefined (1) at the bottom right and no more analysis is being done.

![imagen](https://github.com/StevensND/ghidra-port-mods-guide/assets/45856578/835528ef-9f44-41bf-b9ed-8deac585c6a8)

[CLICK HERE to continue with the guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/GhidraSteps.md)
