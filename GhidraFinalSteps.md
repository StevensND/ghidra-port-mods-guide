# Ghidra Final Steps

Remember when I suggest 2 monitors?. Well ... I did for this step. 

Now let's compare the 2 mains and find which one is the closest to what we are looking for. So in my case in my main monitor I will have the main corresponding to the previous version (1.1.2) and in the other one the main corresponding to the most recent version (1.2.0). 

Click on each of the results that the Search Memory tab gave you and look for a similar structure. In my case it's the second result `710193e484`: I will focus on the purple color. We have: stp, str, mov, ldrb, mov, cbz etc etc. **At the top** we will see a section called **FUNCTION** surrounded by * and below that a **LAB section** where we will find adrp, mov, ldr, str, ldr, ldr, ldr etc etc.

Click on the image below and zoom it. Left side it's 1.1.2 and right side it's 1.2.0

![imagen](https://i.imgur.com/XixhSgr.png)

What does this mean?: That we have found our equivalent code for the new version (1.2.0) and we know that this would be the one we should test first before proceeding with another search and another try. So let’s focus on the FUN section (FUN_710193e484).

Remember that the line of code we are looking for in principle would be:

`710194ea7c 80 02 00 36 tbz w0,#0x0,LAB_710194eacc`

Therefore, we will have to search for the same "Memory" and tbz in our new update.

In this example it would be:

`710193e4b4 80 02 00 36 tbz w0,#0x0,LAB_710193e504`

The Address we need is: `710193e4b4`

Remove the first 2 digits and keep `0193e4b4`

Now we will proceed to make the updated mod.

2. Open [HxD](https://mh-nexus.de/en/downloads.php?product=HxD20). Click on File -> Open. Search for the main file of the latest update (1.2.0 in my case). You can use [this site](https://hexed.it/) too as alternative if you don't want to download HxD.

Open it  and focus on the left corner. Look at 00000040 and 00000050 lines. Get the letters and numbers until you find 0's. That’s the @nsobid that we will need for the update mod. You got a [video explanation here](https://youtu.be/d1XWoEgAgrU)

Here's an example:

![imagen](https://i.imgur.com/smeExqe.png)

For TOTK 1.2.0 it would be: `@nsobid-6F32C68DD3BC7D77AA714B80E92A096A737CDA77`

So … our .pchtxt file should look like this:

![imagen](https://i.imgur.com/NqhxhEE.png)

You can add a line between @flag offset_shift 0x100 and @enable just for info like I did on the screenshot above

And that's it!!. Save the file. Name it 1.2.0 or whatever update it is (be sure the file has .pchtxt extension) and place it into your mods folder. You would already have your mod updated.

![imagen](https://i.imgur.com/YiLWY63.png)

![imagen](https://i.imgur.com/hxXzGlO.png)

![imagen](https://i.imgur.com/dD4ncbq.png)

I hope everything is clear and if you have any questions you can ask me on [Reddit](https://www.reddit.com/user/StevenssND). 

If you want to support me here you have my [Ko-Fi](https://ko-fi.com/stevenss)

Thank you very much and I hope it has helped you. Have fun making ports
