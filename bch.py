#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) < 3:
        print(
            "Usage:\n"
            "  python bch.py <infile> <offset> <patch_data> [output_file]\n\n"
            "Arguments:\n"
            "  <infile>      Path to the binary file to patch\n"
            "  <offset>      Byte offset (decimal) where patch data will be inserted\n"
            "  <patch_data>  is either a path to a patch file or a raw hex string (file takes precedence if it exists)"
            "  [output_file] Optional output filename (default: <infile>_patched)\n\n"
            "Example:\n"
            "  python bch.py firmware.bin 1024 patch.bin firmware_patched.bin\n"
            "  python bch.py firmware.bin 1024 deadbeef\n"
        )
        sys.exit(1)

    infile = sys.argv[1]
    offset = sys.argv[2]
    bytes_arg = sys.argv[3]
    output_file = sys.argv[4] if len(sys.argv) > 4 else sys.argv[1] + "_patched"
    
    try:
        with open(infile, 'rb') as rf:
            with open(output_file, 'wb') as wf:
                chunk_size = 4096
                rf_chunk = rf.read(chunk_size)
                while len(rf_chunk) > 0:
                    wf.write(rf_chunk)
                    rf_chunk = rf.read(chunk_size)
                    
    except FileNotFoundError:
        print(f"Error: File '{infile}' not found.")
        sys.exit(1)

    print("Done")
    
if __name__ == "__main__":
    main()
