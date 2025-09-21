Type the following commands one by one and press Enter after typing

```
set logging enabled on
set logging overwrite on
set architecture aarch64

target extended-remote YOUR SWITCH IP:22225

monitor wait application

attach

c (This means continue)

Control + C (This will freeze the game and you'll be able to type new commands)

x/gx MAIN + Cheat Address
x/wx Result + Jumpback Pointer Address

awatch *

c (This means continue)

x/20i $pc-40