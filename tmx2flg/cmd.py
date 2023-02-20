#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as ET

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--file",required=True, metavar="FILE")
    args = parser.parse_args(argv)

    try:
        tree = ET.parse(args.file)
        root = tree.getroot()
    except:
        print("Can't open file.")
        exit()

    for tileset in root.iter('tileset'):
        # get tileset name for output filename
        name = tileset.get('name')
        # init byte array of size of tileset
        ba = bytearray(int(tileset.get('tilecount')))
        # get tiles in tileset
        for tile in tileset.iter('tile'):
            # get tile ids in tileset
            id = tile.get('id')
            # get flag value (fixme: assumes only one custom property per tile)
            for property in tile.iter('property'):
                flag = property.get('value')
                # store flag value at tile position in array
                ba[int(id)] = int(flag)

        # write out binary file
        with open(name + '.flg', 'wb') as output:
            output.write(ba)

if __name__ == "__main__":
    main()
