#!/usr/bin/env python3

import sys

def is_valid_hex_bytes(s):
    try:
        bytes.fromhex(s)
        return True
    except ValueError:
        return False

def main():
    infile = ""
    offset = 0
    data = bytes.fromhex("")
    output_file = ""
    
    if len(sys.argv) < 4:
        print(
            "Usage:\n"
            "  python bch.py <infile> <offset> <patch_data> [output_file]\n\n"
            "Arguments:\n"
            "  <infile>      Path to the binary file to patch\n"
            "  <offset>      Byte offset (decimal) where patch data will be inserted\n"
            "  <patch_data>  is either a path to a patch file or a raw hex string (file takes precedence if it exists)"
            "  [output_file] Optional output filename (default: <infile>_patched)\n\n"
            "Example:\n"
            "  python bch.py firmware.bin 1024 patch.bin firmware.bin_patched\n"
            "  python bch.py firmware.bin 1024 deadbeef\n"
        )
        sys.exit(1)

    infile = sys.argv[1]
    
    try:
        if int(sys.argv[2]) > 0 :
            offset = int(sys.argv[2])
        else:
            print(f"Error : Invalid offset, must be a positive value.")
            sys.exit(1)
    except ValueError:
        print(f"Error : Invalid offset, not a valid number.")
        sys.exit(1)

        
    try:
        with open(sys.argv[3], 'rb') as df:
            data = df.read()
    except FileNotFoundError:
        if is_valid_hex_bytes(sys.argv[3]):
            data = bytes.fromhex(sys.argv[3])
            print("Patch_data file not found, assuming it's a raw Hex string.")
        else :
            print(f"Error: Patch data is neither a valid Hex Raw value or exists as a file")
            sys.exit(1)
            
    output_file = sys.argv[4] if len(sys.argv) > 4 else sys.argv[1] + "_patched"
    
    try:
        with open(infile, 'rb') as rf:
            with open(output_file, 'wb') as wf:
                ## logic goes here
                pass
    except FileNotFoundError:
        print(f"Error: File '{infile}' not found.")
        sys.exit(1)

    print(f"Done, patched file: {output_file}")

    
if __name__ == "__main__":
    main()
