# Ghidra Steps

1. Open the .pchtxt file of the mod that you want to update/port with [NotePad++](https://notepad-plus-plus.org/downloads/)

For now we are going to focus on the part of 

`@enabled
CODE
@stop`

Being CODE the corresponding code. As an example I would use the following:

`0194EA7C | 14000014`

![imagen](https://i.imgur.com/egkcbbe.png)


**Why I use a separator slash**: The left part will be the Address we need to look up in Ghidra (0194EA7C) while the right part will be the function (14000014) that will perform this Address.

To make the update/port we will never use the right side (14000014). This will always be the same.

Now in Ghidra press the G key (Go To ...) on your keyboard and type/paste the Address obtained in the .pchtxt file. 
Ghidra adds 2 more numbers to this Address at the beginning. Depending on the game this can be 71 or any other number. In total it has to be 10. If it’s less than 10: Ghidra will never find the Address you are looking for. So … I'll search for: 710194EA7C and then click on OK.

![imagen](https://i.imgur.com/4uxXRZA.png)

![imagen](https://i.imgur.com/nlz1nFl.png)

2. Once the Address has been obtained we will have to focus on that whole line of code: `710194ea7c 80 02 00 36     tbz        w0,#0x0,LAB_710194eacc`

To facilitate the understanding of the guide I am using a skin of Ghidra. The white colors will be the Address and the letters and numbers next to the white color will be what we will call "Memory" (I don't know if this is its real name but for clarification we will call it this way). This is represented in blue color.
We will take these numbers/numbers and letters as this is what we will need to update/port the mod. So in my case it will be: `80 02 00 36`

3. We will proceed to open the main of the most recent update (I assume that previously you have already analyzed this main too). Now on our keyboard we will press the S key (Search Memory) and paste the Memory previously obtained (80 02 00 36) and click on Search All.

![imagen](https://i.imgur.com/xs9CcbB.png)

Possibly we will get several results or maybe only 1 depending on the code.  If you have any problem and you get a Search Limit alert go to Edit (next to File) and click on Tools Options then look for the "Search" section and increase the Search Limit (in my case I simply added another 0 at the end). Then click on Apply and then OK and close the tab.

![imagen](https://i.gyazo.com/a7aa46136da777707d1f13c90185fe24.png)

![imagen](https://i.gyazo.com/8d69bcaa47629449c376e5c70b6447df.png)

4. Now that you have obtained several results you will want to know which is the right one ... You have several options: go one by one and see which one is the closest or try to reduce the number of results. In this case I advise you the second option. 

To do this we will add more "Memory" to our search. Try to focus on a single section. That is to say, our whole section would be in this case FUN_710194ea4c and it would end before LAB_710194ea80 so we would add all the possible "Memory" until we reduce our options. 

![imagen](https://i.gyazo.com/2d71ea4964540ebc3a1266c311f01b84.png)


Do it in order as Ghidra shows you. That is to say:

`df 02 00 94 80 02 00 36`

If you don't find a result, discard these options and use the next 2. You have to keep trying to reduce the results as much as possible. For my example: `Address: 710194EA7C`

I had to use all these "Memory": `fd 7b be a9 f3 0b 00 f9 fd 03 00 91 08 00 5f 39` instead

This gave me 2 results. Sometimes you will not find the corresponding "Memory" because a digit may have changed between different versions, so you will have to discard and try other "Memory".

![imagen](https://i.gyazo.com/f163f4b9d7326b8c9a4ef2f6e61da47b.png)

[CLICK HERE to continue with the final steps](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/GhidraFinalSteps.md)

