I do this guide due to **Mario Kart 8 Deluxe** is an old game and it **doesn't have** the typical `7100000000` structure of today's games. 

Also **we can't use Code Updater for Nintendo Switch** due to it will freeze and crash.

So instead of `7100000000` **Mario Kart 8 Deluxe uses** ```60000000```

If you have not yet read the rest of my guides, I advise you to start with [this one](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md) as I'm not going to explain how to setup everything and get the necessary files.

### Structure of the mod that we're going to update as example

```
@nsobid-4B7A0BB5AE57E627B63E2247F9470E57

# Mario Kart 8 Deluxe [0100152000022000] v2.4.0 - 60FPS in Split Screen

@flag print_values
@flag offset_shift 0x100

// Removes Double Buffer from Multi-player modes

@enabled
00B8173C 970000EA
@stop
```

### Steps

1. Open Ghidra, open the Mario Kart 8 Deluxe v2.4.0 main file and press G (Go To ...) in your keyboard. We'll replace our first 0 so that 0 will be 6.

![imagen](https://i.imgur.com/PJHK45k.png)

This is what Ghidra found:

![imagen](https://i.imgur.com/P0hxTtc.png)

2. Now, we'll take the bytes that we'd need for do the Search Memory in the new update (v3.0.1). In this case these bytes will be: `97 00 00 1a`. We will also take `60 02 9f e5` to narrow our search results.

3. Open the v.3.0.1 main file and press S (Search Memory) in your keyboard. Now paste `97 00 00 1a 60 02 9f e5` and set everything like the image below.

![imagen](https://i.imgur.com/sk866Bp.png)

4. Now compare the results from v.2.4.0 and v3.0.1 and see if the structure match or not. Zoom the image below.

![imagen](https://i.imgur.com/6eGoXZY.png)

In this case, everything's OK.

60B8173C bytes are: `97 00 00 1a` and our new address/offset, `60BC0B3C` got the same bytes.
60B81740 bytes are: `60 02 9f e5` and the bytes matches the next new address/offset (we don't need it for this mod): `60BC0B40`

5. Now create the new .pchtxt file using [this guide](https://github.com/StevensND/ghidra-port-mods-guide/blob/main/Ghidra/RyujinxSteps.md) to get the new nsobid, replace the new addresses/offsets and done, you got the mod updated. In this case it will be:

```
@nsobid-9EF5CAA2D5B933C772358C5AA6FABA15

# Mario Kart 8 Deluxe [0100152000022000] v3.0.1 - 60FPS in Split Screen

@flag print_values
@flag offset_shift 0x100

// Removes Double Buffer from Multi-player modes

@enabled
00BC0B3C 970000EA
@stop
```
