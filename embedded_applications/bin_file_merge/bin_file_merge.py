import os
import argparse
import hashlib

offset1 = 0x00100000

def bin_file_merge(bin_file1,bin_file2,bin_merge):
    f1 = open(bin_file1,"rb")
    f2 = open(bin_file2,"rb")
    fmerge = open(bin_merge,"ab")
    
    bin2_size = os.path.getsize(bin_file2)

    data = f1.read()
    fmerge.write(data)
    offset = fmerge.tell()
    data = f2.read()
    #fmerge.seek(offset1)
    fmerge.write(data)
    fmerge.close()




def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('bin_file1', metavar='BIN_FILE1', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('bin_file2', metavar='BIN_FILE2', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('bin_merge', metavar='BIN_MERGE', type=str, nargs=1,
                        help='the directory where to change extension')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    bin_file1 = args['bin_file1'][0]
    bin_file2 = args['bin_file2'][0]
    bin_merge = args['bin_merge'][0]

    bin_success = bin_file_merge(bin_file1,bin_file2,bin_merge)
    print("bin merge success:",bin_success)


if __name__=='__main__':
    main()
