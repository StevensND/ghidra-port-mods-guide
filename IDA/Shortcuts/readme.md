# Shortcuts

These are the shortcuts I use the most in **IDA v.7.7.220118**

**Keep in mind** that when I add the `+` symbol, **you don't have to press it**.

## G key (Jump to address)

![image](https://i.imgur.com/cqzA0EL.png)

As in Ghidra, this key allows us to search for an Offset/Address. In IDA is called `Jump to address`.

## F5 Key (Decompiler)

As in Ghidra, this key allows us to see the `Decompiler`

Here's a [screenshot](https://i.imgur.com/LIFj7GZ.png) of the Decompiler. When you see this message just click on `OK`.

It will display another message, click on `OK` again.

Finally [this is the info](https://i.imgur.com/9e6qMqi.png) that we wanted to see.

## Alt + B (Binary Search) 

![image](https://i.imgur.com/Jo7Y1rj.png)

This is pretty similar to the `S` key on Ghidra (Search Memory).

You can search for bytes as well as for strings. If you are using an older version of IDA you may find it [like this](https://i.imgur.com/C7uFYri.png)

When you want to search for a string, you will have to write the string in quotation marks. Ex: `"SetPresentInterval"`

This will allow us to modify the String encoding. By default it's `UTF-8 (default 8-bit)` but sometimes we will have to change it if we don't find the String.

![image](https://i.imgur.com/e6DpNHv.png)

## Alt + T (Text Search)

![image](https://i.imgur.com/oFqQu6A.png)

This is pretty similar to `Search -> Program Text` on Ghidra (Control + Shift + E)

Type the text that you want to find and enable the `Find all occurences` checkbox, then click on `OK` and wait until it's done.

## Alt + D (Setup data types)

![image](https://i.imgur.com/QAP7YYg.png)

Here we can convert our actual address to byte, double, float etc etc.