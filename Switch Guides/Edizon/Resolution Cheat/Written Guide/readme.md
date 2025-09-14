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

On the `Memory Editor` press B to prepare the jumpback.

![imagen](https://i.imgur.com/lkiAfb7.png)


