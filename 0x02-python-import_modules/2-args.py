#!/usr/bin/python3

if __name__ == "__main__":
    """ printing the arguments passed"""
    import sys
    arr_size = len(sys.argv) - 1
    if arr_size == 0:
        print("0 arguments.")
    elif arr_size == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arr_size))
    for i in range(arr_size):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
