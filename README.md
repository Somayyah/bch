# bch

a tool to safely replace data chunks in binary files without corrupting surrounding data.

## Usage

```
  python bch.py <infile> <offset> <patch_data> <bytes> [output_file]
```

## Arguments

```
  <infile>      Path to the binary file to patch
  <offset>      Byte offset (decimal) where patch data will be inserted
  <patch_data>  is either a path to a patch file or a raw hex string (file takes precedence if it exists)
  <bytes>       How much do you want to replace? 

  [output_file] Optional output filename (default: <infile>_patched)
```

## Examples

```
  python bch.py firmware.bin 1024 patch.bin firmware.bin_patched
  python bch.py firmware.bin 1024 deadbeef
```
