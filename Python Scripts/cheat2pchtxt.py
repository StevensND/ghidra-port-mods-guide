import binascii
import os
import struct
import sys
import re

CHEAT_EXT = ".txt"
CHEAT_ENCODING = "ascii"

PATCH_TEXT_ADDRESS_STRUCT = struct.Struct('>I')

def reverse_hex_string(in_string):
    out_hex_array = []
    for i in range(0, int(len(in_string) / 2)):
        out_hex_array.append(in_string[i * 2] + in_string[(i * 2) + 1])
    out_hex_string = "".join(out_hex_array[::-1])
    return out_hex_string

def generate_output_filename(base_name):
    index = 1
    while True:
        new_name = f"{base_name} ({index}).txt"
        if not os.path.exists(new_name):
            return new_name
        index += 1

def convert_cheat_to_pchtxt(cheat_path, cheat_name, out_pchtxt_path):
    cheat_file = open(cheat_path, 'rt')

    if out_pchtxt_path:
        out_pchtxt_file = open(out_pchtxt_path, 'wb+')
    else:
        out_pchtxt_path = generate_output_filename("PCHTXT Converted")
        out_pchtxt_file = open(out_pchtxt_path, 'wb+')

    for line in cheat_file.readlines():
        codeMatch = re.match(r"^(04000000|040A0000|040E0000)\s+([0-9A-Fa-f]+)\s+([0-9A-Fa-f]+)", line)
        if codeMatch:
            cheat_type = codeMatch.group(1)
            address = codeMatch.group(2)
            value = codeMatch.group(3)

            out_pchtxt_file.write(f"{address} {reverse_hex_string(value)}\n".encode(CHEAT_ENCODING))

    out_pchtxt_file.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: convert_cheat_to_pchtxt.py <cheat_path> [cheat_name] [pchtxt_path]")
    else:
        cheat_name = "Cheat"
        out_pchtxt_path = None
        cheat_path = sys.argv[1]
        if len(sys.argv) > 2:
            cheat_name = sys.argv[2]
        if len(sys.argv) > 3:
            out_pchtxt_path = sys.argv[3]

        convert_cheat_to_pchtxt(cheat_path, cheat_name, out_pchtxt_path)