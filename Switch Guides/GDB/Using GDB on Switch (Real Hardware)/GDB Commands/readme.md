Type the following commands one by one and press after the type:

```
set logging enabled on
set logging overwrite on
set architecture aarch64

target extended-remote YOUR SWITCH IP:22225

monitor wait application

attach

x/gx MAIN + Cheat Address
x/wx Result + Jumpback Pointer Address

awatch

x/20i $pc-40