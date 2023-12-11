# IDA PRO

This is IDA:

![image](https://i.imgur.com/QGIKjqv.png)

As you can see I got `DATA XREF: sub_71002B9E14+1A4` and `sub 71002B9E14+1B8`  

You can click on any of the 2.

However `rodata.2:00000071029B5108` modifies this at the same time.

I suggest you to click on `rodata.2:00000071029B5108` and then press `Alt D` on your keyboard and click on `Float`. 

Now we will see this info: `flt_71029B5108  DCFS 1.7778`. Now please, save the datebase.

Do you remember when I searched for `1.77777802` instead of `1.777777791` or `1.777777777`? ... Well, it was because of this.

Now ... how do I know the float value of other ARs other than 16:9, 21:9, 16:10 or 32:9?

Simply divide ... 16/10 = 1.6, 21/9 = 2,3333 ...

Now go to the [ArmDeveloper site](https://developer.arm.com/documentation/ka001136/latest) and check the table ...

In this case 21/9 = 2,3333 ... However 2,3333 is not in the table. It's between `2.25000000` and `2.37500000`

You have to take the nearest or closest value, in this case `2.375`. But in the case of Mario Wonder, we need the true float, which in this case is `2.33333333`.

So our mod will be:

```
@nsobid-F91868B88F60D3D59009DB3389FDE314A6A32FCD

# Super Mario Bros. Wonder [010015100B514000] v1.0.1 - 21:9 Aspect Ratio

@flag print_values
@flag offset_shift 0x100

// 21:9 Aspect Ratio

@enabled
029B5108 54551540
@stop

@StevensND
@KeatonTheBot

https://linktr.ee/stevenssv2
https://linktr.ee/keatonthebot
```

But what happens if I got something like this?:

```
71002b9fcc ldr s3,[x8, #0x108]
```

In this case I would use [ARMConverter](https://armconverter.com/?code=fmov%20s3,%20%232.37500000) and modify that instruction to: `fmov s3, #2.37500000`.

When we have/want to do fmov, we normally look at the values in the table. So our final code would be:

```
002B9FCC 0370201E
```

# Clean Files

Once you have finished the guide and made the mod: I suggest you delete all generated .txt files including `gdb.txt` from the `bin` folder.

**Before do this**: Backup all the things that you consider important info.

So you would have to delete: `gdb.txt`, `mappings.txt`, `watch_script.txt` and `Ghidra_Offset.txt` from the `bin` folder.

We will do this to avoid possible conflicts the next time we want to repeat the guide.

# End of the guide

That's it, that's the end of the guide. From here on it's just a matter of testing and discovering that each value you have chosen changes according to the instruction you have given it.

I hope it has been useful.

If you have any doubt about the script or if something is not working right ask me or ask Flash in Discord:

`stevenss.` in my case, `fl4sh_` in the other case.