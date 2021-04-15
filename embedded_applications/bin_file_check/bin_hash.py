import os
import argparse
import hashlib

def check_file_hash(bin_file):
    f = open(bin_file,"rb")
    thehash = hashlib.md5()
    theline = f.readline()

    while(theline):
        thehash.update(theline)
        theline = f.readline()

    return thehash.hexdigest()


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('bin_file', metavar='BIN_FILE', type=str, nargs=1,
                        help='the directory where to change extension')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    bin_file = args['bin_file'][0]

    hash_value = check_file_hash(bin_file)
    print("hash_value",hash_value)

if __name__=='__main__':
    main()
