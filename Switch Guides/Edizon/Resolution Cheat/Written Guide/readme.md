**Optional**: Open ReverseNX-Tool and make the game run at Handheld by default.

As I said, this step is optional. Open the homebrew menu and run Reverse-NX Tool.

![imagen](https://i.imgur.com/ycjPsar.png)

For this tutorial, I'm going to mod Hollow Knight: Silksong resolution.

Now select the game, press A, scroll up with the arrows and select Handheld. Then press A.

![imagen](https://i.imgur.com/Lh2DLYn.png)

Check that the game now says Handheld instead of System.

Now run the game, load your save and open Ultrahand/Uberhand by pressing `ZL + ZR + DPAD DOWN` simultaneously to access to the overlay.

Now select `Status Monitor`, press A, scroll down until `Game Resolutions` and press A.

You will see the Game Resolutions Overlay. 

![imagen](https://i.imgur.com/7eV0KpS.png)
![imagen](https://i.imgur.com/w8sbR1r.png)

By default, Silksong runs at 1024x576 on Handheld. Press the HOME button and open the homebrew menu again.

Run Edizon SE.

![imagen](https://i.imgur.com/Rl0UzdH.png)

Edizon SE will open. Then press Y to `Search RAM`

![imagen](https://i.imgur.com/sWUAq7p.png)

Now press L to be able to move between the options.

Be sure that:

```
TYPE is set to u32.
MODE is set to ==
REGION is set to HEAP + MAIN
```

![imagen](https://i.imgur.com/Eu7PPTn.png)

Now press R and set the `VALUE`. In this case 576. After that, move to `Search Now!` and press A.

![imagen](https://i.imgur.com/02E2mEv.png)

You will get the following results. However, we will want to narrow them.

![imagen](https://i.imgur.com/4UuMCxQ.png)

Go back to the game, open Ultrahand/Uberhand overlay and select `ReverseNX-RT`. 

Controlled by system will be set on: `Yes`. Select `Change system control` and press A to change it to `No`

Then, select `Change Mode` and press A. This will change the mode from `Handheld` to `Docked` just like the pic below shows.

![imagen](https://i.imgur.com/7SQPuIL.png)

Now, check the game resolutions again and you'll see that the resolution changed to 1280x720 on Docked.

![imagen](https://i.imgur.com/WOOhVto.png)

Now Press the HOME button, open the homebrew menu and open Edizon again.

On Edizon, press Y to `Search again` and change the `VALUE` to 720. Then select `Search Now!` and press A. This will narrow the results.

![imagen](https://i.imgur.com/KF7AKsH.png)
![imagen](https://i.imgur.com/NZV0xBc.png)

Now go back again to the game, open Ultrahand/Uberhand, select `ReverseNX-RT` and change the mode to `Handheld`.

![imagen](https://i.imgur.com/KGoF942.png)

You can check the `Game Resolutions` again if you want to check that now the resolution changed to `1024x576` again.

Press the HOME button, open the homebrew menu and open Edizon again. 

On Edizon, press Y to `Search again` and change the `VALUE` to 576. Then select `Search Now!` and press A. This will narrow the results again.

Now I only got 3 results and you can see in the pic below. You can repeat this steps if you want to try to narrow the results once again.

However, in this case we can't narrow the results again. It will give 3 results.

Here you have to try each option. In this case, it's the second option that I already have selected, so I'll just press the right joystick.

Pressing the right joystick means open the `Memory Editor`

![imagen](https://i.imgur.com/EcqeDQy.png)

Below, you can see the options that you have. Select the one ending in `400` and press A to `Edit the value`.

Type 1280 and press A. Select the one ending in `240` and press A. Type`720` and press A.

This will change our values to `500` and `2D0` as you can see in the following pic

![imagen](https://i.imgur.com/Z2RlbDM.png)

Now go back to the game, be sure that you have the `Game Resolutions` overlay open and check the resolution. As you can see now we have `1280x720` on Handheld.

![imagen](https://i.imgur.com/AYRdRM3.png)

However, **we can't do the cheat yet**. If we close the game the resolution will go back to `1024x576`. We need to do a Jumpback.

Go back to Edizon SE and open the `Memory Editor` again. 

On the `Memory Editor`, select the one ending in `2D0` and press B to prepare the jumpback.

![imagen](https://i.imgur.com/lkiAfb7.png)

When you see the options, press R, `Page Down`, until you see the first `Main +` result. In this case `Main + 078883F0` 

>[!NOTE]
Remember that were setting the height (720). 720 = 2D0.

If we want to set the width, we'll need to select another `Main +`. 

We will also have to do this if we want to change the Docked resolution. This means another `Main +` to set 1920 and another one to set `1080`.

![imagen](https://i.imgur.com/chky6Ih.png)

Now press Y to `Pick Source`. Now look at the pic below.

![imagen](https://i.imgur.com/rEDCw1b.png)

Press R to `Forward` until you see again the `500` and `2D0`

Now you'll see that you have something like `z=01 main+78883F0(38CA404FC0)+AFE4`

Select `2D0` and press the + button to add a bookmark (BM add). Enter a label and press + again.

You'll see a notification saying `Adress added to bookmark!`

![imagen](https://i.imgur.com/20w59dF.png)

Now Press `ZL + B` to quit. After that press `L` (BM toggle).

You'll see two bookmars. The one we need is the second one.

![imagen](https://i.imgur.com/KIfnP3b.png)

Now press `ZL + A` to Add Cheat. This will create the cheat.

![imagen](https://i.imgur.com/CXHE4fy.png)

Now go back to the game, open Ultrahand/Uberhand and select `Edizon`

![imagen](https://i.imgur.com/t2krNY8.png)

Press A and you'll see all the available cheats that you have. Press A again to enable the cheat.

![imagen](https://i.imgur.com/Iq5xJtU.png)

Check the `Game Resolutions` overlay again and you will see that now the height is set to `720`

Go back to Edizon SE. In case you don't see the bookmarks, press L again. Select the second bookmark and press the right joystick to open the `Memory Editor`

Here, select the one ending in `400` and press B to prepare the Jumpback

![imagen](https://i.imgur.com/cCT5XLm.png)

Now it's your time to choose another `Main +` different from the one we previously choosed before. This will set our width.

![imagen](https://i.imgur.com/9e9StzH.png)

Now change the value again to 1280 (500). Press + to add the bookmark, enter the label, press `ZL + B` to quit and press `L` in case that you don't see the bookmarks.

Select the second option again.

![imagen](https://i.imgur.com/ySG871s.png)

Press `ZL + A` to add the cheat and go back to the game. Open the `Game Resolutions` overlay and check the resolution.

Now the game should be properly set to `1280x720`.

Now back to Edizon SE, move to the cheats tab by moving the left joystick to the left, select the cheats and press the ZL + left joystick to `Write To File`

![imagen](https://i.imgur.com/JJQLCiz.png)

We're done. Now you can do a test by closing the game, run the game again and open Ultrahand/Uberhand. Select Edizon and enable the cheats.

Check the resolution again with the `Game Resolutions` overlay. If it's `1280x720` you're good.

Now it's time to move to our PC. Use DBI with the `MT Responder` option, or a `FTP Client` or just plug your SD card into your PC.

On your SD card, open the `atmosphere folder`.

Now follow the following path:

`atmosphere/contents/010013C00E930000/cheats` you should see two files. One with the BID of your game update and other named toggles.

Drag the one that is not toggles into your desktop and edit the file with Notepad or Notepad++. You'll see something like this:

```
[720]
580F0000 078883F0
780F0000 0000AFE4
640F0000 00000000 000002D0
[1280]
580F0000 07891490
780F0000 0000B010
640F0000 00000000 00000500
```

We can merge all together and leave it like this:

```
[720p Handheld - 1080p Docked]
580F0000 078883F0
780F0000 0000AFE4
640F0000 00000000 000002D0
580F0000 07891490
780F0000 0000B010
640F0000 00000000 00000500
```

However for some reason in this game, this doesn't work properly if we want to set 1080p for Docked and 720p for Handheld. Only one will work while the other will keep the default resolution.

So ... to solve this we're going to edit the .txt, leave it like this and save it:

```
[720p Handheld - 1080p Docked]
580F0000 078883F0
780F0000 0000AFE4
640F0000 00000000 00000000
```

640F0000 00000000 00000000 is appling 720p for Handheld and 1080p for Docked, which means at the end ... we only needed 1 `Main +` also known as address/offset.

This applies to this case; I don't know if the same thing happens in other games. 

**This will correctly apply the resolution changes.**

And that's all folks ... That's how you create the resolution cheat :)

Check the [video guide](https://youtu.be/iuWUp14wN08?si=ZlzrYiF_ukTWNfKz) if you still have doubts.