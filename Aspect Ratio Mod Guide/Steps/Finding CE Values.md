# Basic concepts that you MUST know before starting the guide

Understanding these concepts is **basic to this guide**. If after the explanation you are not able to understand it, **please don't continue** with the guide.

**What is an address/offset**:

To understand this I'm going to take the next screenshot as example:

![imagen](https://i.imgur.com/egkcbbe.png)

Let's represent this screenshot as follows:

`0194EA7C ||||| 14000014`

**Why I use a separator slash**: 

The left part will be the **Address or Offset** that we need to look up in Ghidra **(0194EA7C)** while the right part will be the instruction **(14000014)** that we will give to this Address/Offset.

Normally Ghidra offsets will start with 71 (**NOTE**: not always. There are some older games that can start with different numbers).

Let's take a look at the next Ghidra screenshot:

![imagen](https://i.imgur.com/t7A8bRV.png)

Look at the colors:

- The column starting with 71, **shown in white**, would be all our Ghidra offsets.

- The rest of the columns and colors would represent our instruction.

**In order to make our mod, we need to know the Ghidra offset or address.** 

At first, we don't know it, **that's why we will use Cheat Engine + GDB and some scripts made in Python to find out this offset/address**.

Otherwise, if we knew it directly, we wouldn't be using Cheat Engine + GDB and we would only use Ghidra.

# Finding CE Values

We're going to start opening Yuzu and Cheat Engine.

Remember to have the `Enable GDB Stub` checkbox **enabled** on Yuzu and the `MEM_MAPPED` checkbox **enabled** on Cheat Engine. Otherwise it won't work.

For this guide I'm going to use `Super Mario Wonder v1.0.1` due to I have the values that I need written down as well as the mod done.

The first time you open Yuzu you will see the loading screen in a loop. Don't worry. This is totally normal.

It means that Yuzu is trying to connect to the GDB server.

![image](https://i.imgur.com/S08JSWU.png)

Now it's time to **open gdb-multiarch**. Locate your `gdb-multiarch` folder, then open the `bin` folder and finally run `gdb-multiarch.exe`

You'll see the gdb-multiarch console:

![image](https://i.imgur.com/L55T4rY.png)

Grab our [MAIN COMMANDS](https://github.com/StevensND/ghidra-port-mods-guide/tree/main/Aspect%20Ratio%20Mod%20Guide/Info/Commands) and **copy & paste them** into the `gdb-multiarch console`. Then **Press Enter**. You'll see a warning message. Don't worry, just `Press C` key and Enter (if it's neccesary).

![image](https://i.imgur.com/ZoNAfrL.png)

Now GDB and Yuzu are connected. Go back to Cheat Engine and click on the Magnifying Glass icon.

This will open the `Process List`. Select Yuzu and click on `Open`.

![image](https://i.imgur.com/cHRREoD.png)

Now we got GDB + Yuzu + CE connected. I'm going to start a level on Super Mario Wonder. In this case it will be `Sunbaked Desert Palace`.

On Cheat Engine, I will change `Value Type` to Float and on the Value Box, I will type: `1.77777802`.

Most of the games doesn't always use `1.77777802`. It can be:

```
1.77778029
1.7777802
1.777780
1.7777
1.7777777
1.777777791
```

I'm using `1.77777802` due to I know this is the value that I'm looking for. However you'd need to try: `1.777777791` first. After typing the value click on `First Scan`.

If it doesn't find anything, then test `1.7777777`. If it doesn't find anything then try: `1.7777` etc etc until you find something. 

![image](https://i.imgur.com/0KOGcoF.png)

Click `Next Scan` until no more results appear. Once no more results appear, select all those results and click on the `red arrow` 

Those results will be copied to the bottom and we can start modifying values.

![image](https://i.imgur.com/5xNmZA0.png)

You can go 1 by 1 or select a small group and change the value. 

To do this click on the first value and **while holding down** the `Shift key`, click on the last result you want to choose.

Then Press Enter and type a random value such as 5. Check if the [Aspect Ratio has changed](https://i.imgur.com/bztZdSh.png) in the game.

**DISCLAIMER**: If none of the addresses that CE has found change the aspect ratio, this means that the game cannot change the aspect ratio due to the engine and therefore, this is "the end" of the tutorial. 

```
You can't do anything else. However, later we will see another possible alternative using Ghidra
```

[Click here](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Aspect%20Ratio%20Mod%20Guide/Steps/GDB%20to%20Ghidra.md#final-tips) if this is your case.

In this case the Aspect Ratio has changed so now within the range of values that I have selected I will change the value 1 by 1 until I find which is the Address that makes the Aspect Ratio change.

I have located the value so what I will do is right click on the value and then click on Change Color. I choose the color (red in my case) and continue looking for the next value.

We need 2 values that change the Aspect Ratio. The first one we have already found.

![image](https://i.imgur.com/gBALvhs.png)

Once the second value is located, I will change the 2 values to `2.377777815` or `4.555555344`.

Now we will do a new search and look for this value, so we will repeat the process we have done before until we find no more values.

We will focus on the last 3 digits of our 2 Addresses. In my case: 108.

We will discard these 2 Addresses since we already have them added and add the others below (by selecting them and clicking on the red arrow)

Select the values that don't match 108, press Enter and type a random value like 3

![image](https://i.imgur.com/ZWctg5h.png)

If the values haven't changed and are still `2.377777815` or `4.555555344` it means that it's correct and that these addresses are linked to our addresses ending in 108. 

To test, we will select one of our 2 addresses, change the value to 5 for example and see if all the values in the list have changed to 5.

By doing this we will confirm that these 2 addresses are the ones we need to find our Address in GDB.

**Return the values to `2.377777815` or `4.555555344`** on CE. This is very important. 

If you don't do this, GDB will not be able to find the information that the scripts are giving you.

Also write down the 2 addresses somewhere, in my case: `2650E339108` and `265925B9108`.

We are done with the CE steps, next we will start using [Python scripts](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Aspect%20Ratio%20Mod%20Guide/Steps/Using%20Python%20Scripts.md).