#!/usr/bin/env python3

import argparse
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python bch.py <file> <offset> <hex-bytes>")
        sys.exit(1)

    file = sys.argv[1]
    offset = sys.argv[2]
    bytes_arg = sys.argv[3]

    with open(file, 'rb') as f:
        f_content = f.read()
        print(f_content)


if __name__ == "__main__":
    main()
