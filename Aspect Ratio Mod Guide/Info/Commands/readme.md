Our **main commands** will be:

```set logging enabled on
set logging overwrite on
set architecture aarch64
target extended-remote 192.168.X.Y:6543
```
**Replace X & Y** with your Full Ip Address. 

To know our IP Address: **Open the Windows Menu** and type `cmd`. 

![imagen](https://i.imgur.com/CUrLn6p.png)

Now type `ipconfig` and focus on the `IPv4 Address` section. Copy and paste those numbers somewhere and finish typing the `target extended-remote` command correctly. `Eg: 192.168.1.169`

Our **second commands** will be:

```
monitor get mappings
monitor get info
```

`monitor get mappings` is necessary for our Python script to generate the commands and information we will need to get our address in GDB.

`monitor gef info` will display info of the differents regions of the game such as Alias, Heap, Aslr, Stack ...

Our **final** command will be:

```
x/20i $pc-40
```

We use this command to display the instructions around our address as the [Fruithapje21's Guide said](https://www.reddit.com/r/totkmods/comments/149lpz5/comment/jriqx7f/?context=3) and locate our GDB Address to be converted.