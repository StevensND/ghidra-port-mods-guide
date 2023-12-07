# Made with <3 by systemdev on GBATemp

def reverse_hex_string(in_string):
    out_hex_array = []
    for i in range(0, int(len(in_string) / 2)):
        out_hex_array.append(in_string[i * 2] + in_string[(i * 2) + 1])
    out_hex_string = "".join(out_hex_array[::-1])
    return out_hex_string

def collect_and_print_reversed_hex_strings():
    reversed_hex_strings = []
    while True:
        inHexString = input("Enter your hex string (Leave the 0x out), or type 'pause' to print hex strings, or 'exit' to close: ")

        if inHexString.lower() == 'exit':
            break
        elif inHexString.lower() == 'pause':
            print("\nReversed Hex Strings:")
            for reversed_hex in reversed_hex_strings:
                print(reversed_hex)
            input("\nPress Enter to continue...")
        else:
            outHexString = reverse_hex_string(inHexString)
            reversed_hex_strings.append(outHexString)

    print("Exiting the script...")

if __name__ == "__main__":
    collect_and_print_reversed_hex_strings()